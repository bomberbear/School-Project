cd ./db/

# Check if Docker service is running
if ! systemctl is-active --quiet docker; then
    echo "Starting docker service. Asking user for root..."
    sudo systemctl start docker
fi

# Run the container
docker compose up -d

# Get the container ID
container_id=$(docker ps -q -f name=Automated_Labeling_System)

# Get the log of the container
echo "Waiting for db to respond..."
status=$(docker inspect -f {{.State.Health.Status}} $container_id)

# Wait for mariadb to finish initializing
while ! [[ $status == "healthy" ]]; do
  sleep 1
  status=$(docker inspect -f {{.State.Health.Status}} $container_id)
done

# Start the python program
cd ..
python3 ./app/main.py

# Stop the docker container
docker stop $container_id 1> /dev/null