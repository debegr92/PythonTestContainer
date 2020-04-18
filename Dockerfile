# Start with the basic Python3 container
FROM python:3

# Define all optional environment parameters
ENV OPTIONAL defaultValue

# Add all needed Python scripts
ADD test.py /

# Start python script with verbose output, so that all messages are printed in the container
ENTRYPOINT ["sh", "-c", "python -u /test.py -r ${REQUIRED} -o ${OPTIONAL}"]
