import subprocess, os, time, sys

def start(sleep_time: int = 5):
    print("Starting database...")

    docker_command = "docker compose up -d"
    original_dir = os.getcwd()
    dest_dir = os.path.join(original_dir, "db")

    try:
        os.chdir(dest_dir)
        proc = subprocess.Popen(docker_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(sleep_time)

    except FileNotFoundError:
        print("Error: docker engine is not installed.",
              file=sys.stderr)
        exit(1)

    # check if container is running
    db_check_command = "docker ps"
    container_name = "Automated_Labeling_System"
    db_check = subprocess.Popen(db_check_command, shell=True, stdout=subprocess.PIPE)
    output, error = db_check.communicate()

    if not bytes(container_name, "UTF8") in output:
        print("Error: Container is not running.",
              file=sys.stderr)
        exit(1)

    os.chdir(original_dir)