import os
import subprocess
import time

# Get the current working directory
project_dir = os.getcwd()

# Function to create the virtual environment and install dependencies using Poetry
def setup_project():
    # Ensure Poetry is configured to create the virtualenv in the project directory
    subprocess.run(["poetry", "config", "virtualenvs.in-project", "true"], cwd=project_dir)

    # Create the virtual environment
    subprocess.run(["poetry", "env", "use", "python3"], cwd=project_dir)  # Ensure a Python version is specified
    
    # Install dependencies (ensure there's something in your `pyproject.toml`)
    subprocess.run(["poetry", "install"], cwd=project_dir)

# Function to register a Jupyter kernel with the created virtual environment
def register_kernel():
    # Wait for a moment to ensure the virtual environment is created
    time.sleep(2)

    # Get the path to the virtual environment created by Poetry
    poetry_env_path = os.path.join(project_dir, ".venv")  # Assuming `.venv` is created in the project directory

    # The kernel name can be created using the project name
    kernel_name = "{{ cookiecutter.project_name | replace(' ', '_') }}-env"
    
    # Check if the virtual environment exists before proceeding
    if os.path.exists(poetry_env_path):
        # Register the Jupyter kernel with the virtual environment's Python executable
        subprocess.run([
            os.path.join(poetry_env_path, 'bin', 'python'),
            "-m", "ipykernel", "install",
            "--user",
            "--name", kernel_name,
            "--display-name", kernel_name
        ])
    else:
        print(f"Virtual environment not found at {poetry_env_path}")

if __name__ == "__main__":
    setup_project()  # Create the virtual environment and install dependencies
    register_kernel()  # Register the Jupyter kernel
