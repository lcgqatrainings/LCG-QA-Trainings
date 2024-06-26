import xml.etree.ElementTree as ET
import os


def update_readme_with_scores(test_results_file, readme_file):
    if not os.path.exists(readme_file):
        with open(readme_file, 'w') as file:
            file.write("# Assignment Scores\n\n## Scores\n\n")

    tree = ET.parse(test_results_file)
    root = tree.getroot()
    total_tests = int(root.attrib['tests'])
    failures = int(root.attrib['failures'])
    errors = int(root.attrib['errors'])
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
                file.write(f'| Metric     | Count |\n')
                file.write(f'|------------|-------|\n')
                file.write(f'| Total Tests| {total_tests} |\n')
                file.write(f'| Passed     | {passed} |\n')
                file.write(f'| Failures   | {failures} |\n')
                file.write(f'| Errors     | {errors} |\n')
                file.write(f'| Score      | {score:.2f}% |\n\n')
            elif score_section and line.strip() == "":
                score_section = False
            if not score_section:
                file.write(line)


if __name__ == "__main__":
    update_readme_with_scores('test-results.xml', 'README.md')
