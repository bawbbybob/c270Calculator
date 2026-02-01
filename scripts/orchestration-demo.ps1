# Docker Swarm Orchestration Demo Script
# This script demonstrates Docker Swarm capabilities: deployment, scaling, and high availability

Write-Host "=== Docker Swarm Orchestration Demo ===" -ForegroundColor Cyan
Write-Host ""

# Step 1: Initialize Docker Swarm (only needed once)
Write-Host "Step 1: Initializing Docker Swarm..." -ForegroundColor Yellow
Write-Host "Command: docker swarm init" -ForegroundColor Gray
docker swarm init
Write-Host "✓ Docker Swarm initialized" -ForegroundColor Green
Write-Host ""

# Pause for user to see output
Read-Host "Press Enter to continue to building the image"

# Step 2: Build the image
Write-Host "Step 2: Building Docker image..." -ForegroundColor Yellow
Write-Host "Command: docker build -t c270calcapp:latest ." -ForegroundColor Gray
docker build -t c270calcapp:latest .
Write-Host "✓ Image built successfully" -ForegroundColor Green
Write-Host ""

# Pause for user to see output
Read-Host "Press Enter to continue to deploying the stack"

# Step 3: Deploy the stack with 3 replicas
Write-Host "Step 3: Deploying stack with 3 replicas..." -ForegroundColor Yellow
Write-Host "Command: docker stack deploy -c docker-compose.yml yesdaddy-calc-stack" -ForegroundColor Gray
docker stack deploy -c docker-compose.yml yesdaddy-calc-stack
Write-Host "✓ Stack deployed" -ForegroundColor Green
Write-Host ""

# Pause for deployment to stabilize
Write-Host "Waiting 5 seconds for containers to start..."
Start-Sleep -Seconds 5

# Step 4: Verify it's running
Write-Host "Step 4: Verifying services are running..." -ForegroundColor Yellow
Write-Host "Command: docker service ls" -ForegroundColor Gray
docker service ls
Write-Host ""
Write-Host "Detailed service status:" -ForegroundColor Yellow
Write-Host "Command: docker service ps yesdaddy-calc-stack_calculator-app" -ForegroundColor Gray
docker service ps yesdaddy-calc-stack_calculator-app
Write-Host "✓ Services running" -ForegroundColor Green
Write-Host ""

# Pause for user to see output
Read-Host "Press Enter to start the scaling demo (the impressive part!)"

# Step 5: Demo scaling UP
Write-Host "Step 5a: SCALING UP - Increasing replicas to 5..." -ForegroundColor Yellow
Write-Host "Command: docker service scale yesdaddy-calc-stack_calculator-app=5" -ForegroundColor Gray
docker service scale yesdaddy-calc-stack_calculator-app=5
Write-Host ""
Write-Host "Current services:" -ForegroundColor Yellow
docker service ls
Write-Host ""
Write-Host "All 5 replicas:" -ForegroundColor Yellow
docker service ps yesdaddy-calc-stack_calculator-app
Write-Host "✓ Successfully scaled to 5 replicas" -ForegroundColor Green
Write-Host ""

# Pause for user to see scaling
Read-Host "Press Enter to scale down to 2 replicas"

# Step 5b: Demo scaling DOWN
Write-Host "Step 5b: SCALING DOWN - Decreasing replicas to 2..." -ForegroundColor Yellow
Write-Host "Command: docker service scale yesdaddy-calc-stack_calculator-app=2" -ForegroundColor Gray
docker service scale yesdaddy-calc-stack_calculator-app=2
Write-Host ""
Write-Host "Current services:" -ForegroundColor Yellow
docker service ls
Write-Host ""
Write-Host "Remaining 2 replicas:" -ForegroundColor Yellow
docker service ps yesdaddy-calc-stack_calculator-app
Write-Host "✓ Successfully scaled down to 2 replicas" -ForegroundColor Green
Write-Host ""

# Pause for user to see scaling
Read-Host "Press Enter to scale back to 3 replicas (original)"

# Step 5c: Return to 3 replicas
Write-Host "Step 5c: Scaling back to original 3 replicas..." -ForegroundColor Yellow
Write-Host "Command: docker service scale yesdaddy-calc-stack_calculator-app=3" -ForegroundColor Gray
docker service scale yesdaddy-calc-stack_calculator-app=3
Write-Host ""
Write-Host "Current services:" -ForegroundColor Yellow
docker service ls
Write-Host ""
Write-Host "Final 3 replicas:" -ForegroundColor Yellow
docker service ps yesdaddy-calc-stack_calculator-app
Write-Host "✓ Successfully scaled back to 3 replicas" -ForegroundColor Green
Write-Host ""

Write-Host "=== Demo Complete ===" -ForegroundColor Cyan
Write-Host "The application is running at: http://localhost:8080" -ForegroundColor Green
Write-Host ""
Write-Host "To clean up (remove the stack):" -ForegroundColor Yellow
Write-Host "  docker stack rm yesdaddy-calc-stack" -ForegroundColor Gray
Write-Host ""
Write-Host "To disable Swarm entirely:" -ForegroundColor Yellow
Write-Host "  docker swarm leave --force" -ForegroundColor Gray
