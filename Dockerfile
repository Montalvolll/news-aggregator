# Use an official Python runtime as the base imagey
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

# Expose the port that the app runs on
EXPOSE 5000

# Set the command to run the application
CMD ["python", "app/app.py"]