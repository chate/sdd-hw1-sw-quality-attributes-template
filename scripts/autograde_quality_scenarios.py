import re
from pathlib import Path

FILE = Path("quality_scenarios.md")
score = 0
MAX_SCORE = 35

def is_filled(text):
    text = text.strip()
    if not text:
        return False
    if "_" * 5 in text:
        return False
    return True

if not FILE.exists():
    print("❌ quality_scenarios.md not found")
    print("Score: 0/35")
    exit(0)

content = FILE.read_text(encoding="utf-8")

score += 5  # file exists

student_fields = ["ชื่อ-นามสกุล", "รหัสนิสิต", "Section", "วันที่"]
student_ok = True

for field in student_fields:
    m = re.search(rf"\*\*{field}\*\*:\s*(.+)", content)
    if not m or not is_filled(m.group(1)):
        student_ok = False

if student_ok:
    score += 5

system_match = re.search(r"\*\*ระบบที่เลือก\*\*:\s*(.+)", content)
desc_match = re.search(r"\*\*คำอธิบายสั้นๆ\*\*:(.*?)-{3,}", content, re.S)

if system_match and is_filled(system_match.group(1)) and desc_match:
    if is_filled(desc_match.group(1)):
        score += 5

scenario_fields = ["Attribute", "Source", "Stimulus", "Artifact", "Environment", "Response"]
scenario_ok = True

for field in scenario_fields:
    m = re.search(rf"\*\*{field}\*\*:\s*(.+)", content)
    if not m or not is_filled(m.group(1)):
        scenario_ok = False

if scenario_ok:
    score += 10

sentence_match = re.search(r"\*\*เขียนเป็นประโยค\*\*:(.*?)-{3,}", content, re.S)
if sentence_match and is_filled(sentence_match.group(1)):
    score += 5

response_match = re.search(r"\*\*Response\*\*:\s*(.+)", content)
if response_match and re.search(r"\d", response_match.group(1)):
    score += 5

PASSING_SCORE = 25

print(f"Score: {score}/{MAX_SCORE}")

if score < PASSING_SCORE:
    exit(1)

