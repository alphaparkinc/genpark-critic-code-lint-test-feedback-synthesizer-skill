from client import LintFeedbackSynthesizer

feedback = LintFeedbackSynthesizer.synthesize_feedback("", "SyntaxError: unexpected EOF while parsing", 1)
print("Diagnostic Feedback:\n", feedback)
