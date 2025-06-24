# Use official Python image
FROM python:3.10
 
# Set working directory
WORKDIR /app
 
# Copy files
COPY requirements.txt .
COPY app.py .
 
# Install dependencies
RUN pip install -r requirements.txt
 
# Run the application
CMD ["python", "app.py"]