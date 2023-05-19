import os
from pathlib import Path

from GithubBackup import GithubBackup
from utils import create_logger

if __name__ == "__main__":
    logger = create_logger("github-backup")

    # Parse environment variables
    logger.info("Parsing environment variables")
    username = os.getenv("GITHUB_USERNAME", "")
    if username == "":
        logger.error("You must provide a GITHUB_USERNAME environment variable!")
        exit(1)

    access_token = os.getenv("GITHUB_ACCESS_TOKEN", "")
    if access_token == "":
        logger.error("You must provide a GITHUB_ACCESS_TOKEN environment variable!")
        exit(1)

    destination_dir = os.getenv("DESTINATION_DIR", ".")
    destination_dir = Path(destination_dir)
    destination_dir.mkdir(parents=True, exist_ok=True)

    exclude_repos_list = os.getenv("EXCLUDE_REPOS_LIST", "").split(",")
    exclude_forks = os.getenv("EXCLUDE_FORKS", "False") != "False"

    github_backup = GithubBackup(username, access_token, exclude_repos_list, exclude_forks)
    logger.info("Starting backup")
    github_backup.backup(destination_dir)

    logger.info("Backup successfully finished!")
