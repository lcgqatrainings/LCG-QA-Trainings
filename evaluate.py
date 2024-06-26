import xml.etree.ElementTree as ET
import os
from tabulate import tabulate

def update_readme_with_scores(test_results_file, readme_file):
    # Clear the README file content
    with open(readme_file, 'w') as file:
        file.write("# Assignment Scores\n\n")
        file.write("## Scores\n\n")
        file.write("| Metric      | Count |\n")
        file.write("|-------------|-------|\n")
        file.write("| Total Tests | -     |\n")
        file.write("| Passed      | -     |\n")
        file.write("| Failures    | -     |\n")
        file.write("| Errors      | -     |\n")
        file.write("| Score       | -     |\n\n")
        file.write("## Test Results\n\n")
        file.write("| Test Name                | Status | Assertion |\n")
        file.write("|--------------------------|--------|-----------|\n")

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
        file.write('## Scores\n\n')
        file.write('| Metric      | Count |\n')
        file.write('|-------------|-------|\n')
        file.write(f'| Total Tests | {total_tests:<5} |\n')
        file.write(f'| Passed      | {passed:<5} |\n')
        file.write(f'| Failures    | {failures:<5} |\n')
        file.write(f'| Errors      | {errors:<5} |\n')
        file.write(f'| Score       | {score:.2f}% |\n\n')

        # Gather test case results
        test_results = []
        for testcase in testsuite.findall('testcase'):
            test_name = testcase.attrib['name']
            test_status = "Passed"
            assertion = ""
            failure_elem = testcase.find('failure')
            error_elem = testcase.find('error')
            if failure_elem is not None:
                test_status = "Failed"
                assertion = failure_elem.text.strip().replace("\n", " ").replace("  ", " ")
            elif error_elem is not None:
                test_status = "Error"
                assertion = error_elem.text.strip().replace("\n", " ").replace("  ", " ")

            test_results.append([test_name, test_status, assertion])

        # Use tabulate to format the test results table
        table = tabulate(test_results, headers=["Test Name", "Status", "Assertion"], tablefmt="pipe")
        file.write("## Test Results\n\n")
        file.write(table)
        file.write("\n")


if __name__ == "__main__":
    update_readme_with_scores('test-results.xml', 'README.md')
