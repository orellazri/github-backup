import multiprocessing
import subprocess
import tarfile
import tempfile
from pathlib import Path

from github import Github

from utils import create_logger


class GithubBackup:
    def __init__(self, username: str, access_token: str, exclude_repos_list: list[str], exclude_forks: bool):
        self.username = username
        self.access_token = access_token
        self.exclude_repos_list = exclude_repos_list
        self.exclude_forks = exclude_forks
        self.tmpdir = ""

        self.logger = create_logger("GithubBackup")
        self.github = Github(access_token)

    def backup(self, destination_dir: Path):
        self.logger.info("Creating temporary directory")
        with tempfile.TemporaryDirectory() as self.tmpdir:
            pool = multiprocessing.Pool()

            work = []
            for repo in self.github.get_user().get_repos():
                work.append(repo)

            pool.map(self.clone_repo, work)
            pool.close()
            pool.join()

            self.logger.info("Creating archive")
            with tarfile.open(destination_dir / "github-backup.tar", "w:gz") as tar:
                tar.add(self.tmpdir, arcname="github-backup")

    def clone_repo(self, repo):
        logger = create_logger(repo.name)

        if repo.name in self.exclude_repos_list:
            logger.info(f"Skipping {repo.name} since it's in the exclusion list")
            return

        if self.exclude_forks and repo.fork:
            logger.info(f"Skipping {repo.name} since it's a fork")
            return

        if repo.owner.login != self.username:
            logger.info(f"Skipping {repo.name} since it's not owned by {self.username} (owner: {repo.owner.login})")
            return

        logger.info(f"Cloning {repo.name}")
        try:
            subprocess.check_output(f"git clone https://{self.username}:{self.access_token}@github.com/{self.username}/{repo.name} \
                                    {self.tmpdir}/{repo.name}",
                                    stderr=subprocess.STDOUT,
                                    shell=True)
        except subprocess.CalledProcessError as e:
            logger.error(e.output)
