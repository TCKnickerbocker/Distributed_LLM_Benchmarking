# Dockerfile
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY app /app/

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
