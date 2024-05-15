# Use the official Python image as a base image
FROM python:3.10-slim


# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY src/requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY src/ .

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
