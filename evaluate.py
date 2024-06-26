import xml.etree.ElementTree as ET
import os


def update_readme_with_scores(test_results_file, readme_file):
    if not os.path.exists(readme_file):
        with open(readme_file, 'w') as file:
            file.write("# Assignment Scores\n\n## Scores\n\n")
            file.write("| Metric      | Count |\n")
            file.write("|-------------|-------|\n")
            file.write("| Total Tests | -     |\n")
            file.write("| Passed      | -     |\n")
            file.write("| Failures    | -     |\n")
            file.write("| Errors      | -     |\n")
            file.write("| Score       | -     |\n\n")
            file.write("## Test Results\n\n")
            file.write("| Test Name             | Status  | Assertion |\n")
            file.write("|-----------------------|---------|-----------|\n")

    tree = ET.parse(test_results_file)
    root = tree.getroot()

    # Find the correct testsuite element and extract necessary attributes
    testsuite = root.find('testsuite')
    total_tests = int(testsuite.attrib['tests'])
    failures = int(testsuite.attrib['failures'])
    errors = int(testsuite.attrib['errors'])
    passed = total_tests - failures - errors
    score = (passed / total_tests) * 100

    with open(readme_file, 'r') as file:
        lines = file.readlines()

    with open(readme_file, 'w') as file:
        score_section = False
        for line in lines:
            if line.startswith('## Scores'):
                score_section = True
                file.write(f'## Scores\n\n')
                file.write(f'| Metric      | Count |\n')
                file.write(f'|-------------|-------|\n')
                file.write(f'| Total Tests | {total_tests} |\n')
                file.write(f'| Passed      | {passed} |\n')
                file.write(f'| Failures    | {failures} |\n')
                file.write(f'| Errors      | {errors} |\n')
                file.write(f'| Score       | {score:.2f}% |\n\n')
            elif score_section and line.strip() == "":
                score_section = False
            if not score_section:
                file.write(line)

        # Iterate over testcases and extract detailed test results
        for testcase in testsuite.findall('testcase'):
            test_name = testcase.attrib['name']
            test_status = "Passed"
            assertion = ""  # You need to extract this information from your test results
            failure_elem = testcase.find('failure')
            error_elem = testcase.find('error')
            if failure_elem is not None:
                test_status = "Failed"
                assertion = failure_elem.text.strip()  # Adjust according to your XML structure
            elif error_elem is not None:
                test_status = "Error"
                assertion = error_elem.text.strip()  # Adjust according to your XML structure

            file.write(f'| {test_name.ljust(23)} | {test_status.ljust(7)} | {assertion} |\n')


if __name__ == "__main__":
    update_readme_with_scores('test-results.xml', 'README.md')
