import json, sys

#values_file = input("Введите путь к файлу values.json: ")
#tests_file = input("Введите путь к файлу tests.json: ")
#report_file = input("Введите путь к файлу записи: ")

#values_file = r"C:\Users\Riht\Desktop\Job\Performance Labs\Task 3\values.json"
#tests_file = r"C:\Users\Riht\Desktop\Job\Performance Labs\Task 3\tests.json"
#report_file = r"C:\Users\Riht\Desktop\Job\Performance Labs\Task 3\report.json"

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

with open(values_file) as file:
    values_contents = json.load(file)["values"]

with open(tests_file) as file:
    tests_contents = json.load(file)

def go_through_tests(main_test, main_values):
    for tests in main_test:
        for values in main_values:
            if tests["id"] == values["id"]:
                tests["value"] = values["value"]
            if "values" in tests:
                go_through_tests(tests["values"], main_values)

for tests in tests_contents["tests"]:
    for values in values_contents:
        if tests["id"] == values["id"]:
            tests["value"] = values["value"]
        if "values" in tests:
            go_through_tests(tests["values"], values_contents)

with open(report_file, 'w') as file:
    json.dump(tests_contents, file)
