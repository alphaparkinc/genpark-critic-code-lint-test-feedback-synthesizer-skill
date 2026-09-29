"""Critic Code Lint & Test Feedback Synthesizer.
100% Python Standard Library.
"""

class LintFeedbackSynthesizer:
    """Synthesizes compilation errors and linter outputs into targeted repair prompts."""
    @staticmethod
    def synthesize_feedback(stdout: str, stderr: str, exit_code: int) -> dict:
        errors = []
        for line in stderr.splitlines():
            line_str = line.strip()
            if "Error" in line_str or "Exception" in line_str:
                errors.append(line_str)
        
        summary = "Success" if exit_code == 0 else f"Failed with exit code {exit_code}"
        suggestions = []
        for err in errors:
            if "SyntaxError" in err:
                suggestions.append("Check unbalanced brackets, quotes, or missing colons.")
            elif "ImportError" in err or "ModuleNotFoundError" in err:
                suggestions.append("Verify module names; strictly use Python standard library.")
            elif "ZeroDivisionError" in err:
                suggestions.append("Add check for denominator == 0.")
            elif "TypeError" in err:
                suggestions.append("Verify argument count and variable types.")

        return {
            "exit_code": exit_code,
            "status": summary,
            "detected_errors": errors[:5],
            "actionable_suggestions": list(set(suggestions))
        }
