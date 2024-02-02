import argparse
import subprocess


def test_runner(test_path):
    options = [
        'robot',
        '--outputdir', 'results/',
        '--log', 'log.html',
        '--output', 'output.xml',
        '--report', 'report.html',
        test_path
    ]
    return subprocess.run(options)


def parse_args():
    parser = argparse.ArgumentParser(description='Run Robot Framework tests.')
    parser.add_argument('tests_path', help='Path to the Robot Framework tests.')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result = test_runner(args.tests_path)
    message = "Success" if result.returncode == 0 else "Error"
    print(f"Execution result: {message}")
