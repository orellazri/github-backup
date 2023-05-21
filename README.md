<div align="center">

# GitHub Backup

Easily back up your GitHub repositories to a compressed tar file

</div>

[![Push Image](https://github.com/orellazri/github-backup/actions/workflows/docker-image.yml/badge.svg)](https://github.com/orellazri/github-backup/actions/workflows/docker-image.yml)

## Running

### Running with Docker (Recommended)

The recommended way is to use Docker to start a container that runs this program.

```bash
docker run --rm \
    -e GITHUB_USERNAME="..." \
    -e GITHUB_ACCESS_TOKEN="..." \
    -e ... \
    -v $(pwd):/backups \
    reaperberri/github-backup
```

### Running with Python

Clone the repository and run:

```bash
pip3 install -r requirements.txt
# export environment variables here like so:
# DESTINATION_DIR=...
python3 main.py
```

## Environment Variables

| Name                | Description                                                                                                  | Example     |
| ------------------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| GITHUB_USERNAME     | Your GitHub username                                                                                         | orellazri   |
| GITHUB_ACCESS_TOKEN | Your personal access token                                                                                   | ...         |
| EXCLUDE_REPOS_LIST  | (Optional) Comma-separated list of repositories to exclude                                                   | repo1,repo2 |
| EXCLUDE_FORKS       | (Optional) Whether to ignore forks you made                                                                  | True        |
| DESTINATION_DIR     | (Optional) Directory to put the archived file into. **Should only use if not running within a container!**   | /backups    |
