from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old = '''        answers[question] = value;\n\n      });'''
new = '''        answers[question] = value;\n\n        // Final question: show the recommendation immediately after Yes/No.\n        if (currentStep === totalSteps && question === "gas") {\n          setTimeout(showQuizResult, 120);\n        }\n\n      });'''

if old in s:
    s = s.replace(old, new, 1)
    p.write_text(s, encoding='utf-8')
