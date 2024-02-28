import os
import subprocess
from dotenv import load_dotenv

load_dotenv()


def test_runner():
    options = [
        "robot",
        "--pythonpath",
        ".",
        "--outputdir",
        "bifrost/results",
        "--log",
        "log.html",
        "--output",
        "output.xml",
        "--report",
        "report.html",
        f"src/bifrost/tests",
    ]
    return subprocess.run(options)


if __name__ == "__main__":
    result = test_runner()
    message = (
        "Success"
        if result.returncode == 0
        else "Error running test"
    )
    print(f"Execution result: {message}")

    if result.returncode != 0:
        sys.exit(1)
