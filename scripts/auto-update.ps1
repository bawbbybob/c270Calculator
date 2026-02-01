# PowerShell parameters (can be overridden when script is called)
param(
    [string]$RepoPath = "C:\Users\Vi Ann\c270todolist",  # Path to the repository
    [string]$ServiceName = "yesdaddy-calc-stack_calculator-app",  # Docker Swarm service name
    [string]$ImageName = "c270calcapp:latest"  # Docker image name and tag
)

# Strict mode: stops on errors and undefined variables
Set-StrictMode -Version Latest
# Stop execution immediately on error (do not continue)
$ErrorActionPreference = "Stop"

# Change to the repository directory
Set-Location $RepoPath

# Fetch latest commits from remote (GitHub) without changing local branch
git fetch --quiet
# Get the hash of the latest local commit
$localHead = git rev-parse HEAD
# Get the hash of the latest commit on origin/main (remote)
$remoteHead = git rev-parse "origin/main"

# Check if local and remote are out of sync (new changes available)
if ($localHead -ne $remoteHead) {
    # Pull new commits from GitHub (fast-forward only, no merge conflicts)
    git pull --ff-only
    # Rebuild the Docker image with the latest code
    docker build -t $ImageName .
    # Force Docker Swarm to redeploy the service with the new image
    docker service update --force $ServiceName
}

