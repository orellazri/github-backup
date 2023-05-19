<div align="center">

# GitHub Backup

Easily back up your GitHub repositories to a compressed tar file

</div>

## Running

### Running with Docker (Recommended)

The recommended way is to use Docker to start a container that runs this program.

```bash
docker run --rm \
    -e GITHUB_USERNAME="..." \
    -e GITHUB_ACCESS_TOKEN="..." \
    -e ... \
    reaperberri/github-backup
```

### Running with Python

Clone the repository and run:

```bash
pip3 install -r requirements.txt
# export environment variables here like so:
# GITHUB_USERNAME=...
python3 main.py
```

## Environment Variables

| Name                | Description                                                                        | Example       |
| ------------------- | ---------------------------------------------------------------------------------- | ------------- |
| GITHUB_USERNAME     | Your GitHub username                                                               | orellazri     |
| GITHUB_ACCESS_TOKEN | Your personal access token                                                         | ...           |
| DESTINATION_DIR     | (Optional) Directory to put the archived file into - defaults to current directory | /home/backups |
| EXCLUDE_REPOS_LIST  | (Optional) Comma-separated list of repositories to exclude                         | repo1,repo2   |
| EXCLUDE_FORKS       | (Optional) Whether to ignore forks you made                                        | True          |
