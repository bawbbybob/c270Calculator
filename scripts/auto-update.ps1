param(
    [string]$RepoPath = "C:\Users\Vi Ann\c270todolist",
    [string]$ServiceName = "yesdaddy-calc-stack_todolist-app",
    [string]$ImageName = "c270todolist:latest"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Set-Location $RepoPath

git fetch --quiet
$localHead = git rev-parse HEAD
$remoteHead = git rev-parse @{u}

if ($localHead -ne $remoteHead) {
    git pull --ff-only
    docker build -t $ImageName .
    docker service update --force $ServiceName
}
