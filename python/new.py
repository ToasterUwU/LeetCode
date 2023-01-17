import json


leet_code_url = input("URL to leetcode problem: ")

problem_name = (
    leet_code_url.replace("https://leetcode.com/problems/", "")
    .replace("/", "")
    .replace("-", "_")
)

test_class_name = problem_name.replace("_", " ").title().replace(" ", "")

print(
    "Copy and paste the example values and outputs here. Ctrl-D or Ctrl-Z ( windows ) to save it."
)
test_cases_raw = []
while True:
    try:
        line = input()
    except EOFError:
        break
    test_cases_raw.append(line)

test_cases_raw = "\n".join(test_cases_raw)
test_cases = []

lines = test_cases_raw.splitlines()
i = 0
while i < len(lines) - 1:
    if "Example" in lines[i]:
        test_case = {"kwargs": {}, "correct_output": None}

        while not "Input" in lines[i]:
            i += 1

        kwargs = {}
        for pair in lines[i].replace("Input: ", "").split(", "):
            key, val = pair.split(" = ")

            kwargs[key] = json.loads(val)

        test_case["kwargs"] = kwargs

        while not "Output" in lines[i]:
            i += 1

        test_case["correct_output"] = json.loads(lines[i].replace("Output: ", ""))

        test_cases.append(test_case)

    i += 1


with open("test_template.txt", "r") as f:
    template = f.read()

template_values = {
    r"%LEET_CODE_URL%": leet_code_url,
    r"%PROBLEM_NAME%": problem_name,
    r"%TEST_CASES%": json.dumps(test_cases),
    r"%TEST_CLASS_NAME%": test_class_name,
}

for placeholder, value in template_values.items():
    template = template.replace(placeholder, value)

with open(f"src/{problem_name}.py", "w+") as f:
    f.write(f"# {leet_code_url}\nclass Solution:\n")

with open(f"tests/{problem_name}_test.py", "w+") as f:
    f.write(template)
