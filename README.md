
# Python Test Container
This project is a minimal Python 3 script as Docker container.
Everything ready as boilerplate project.
The Python 3 script has two required parameters, but they can be made optional, by providing a default value in the Dockerfile.
You can use the parameters in an external environment file, or directly from your docker-compose YAML file.

## Docker
Open command line in the root folder of this project.
`cd PythonTestContainer`

### Build Docker Container
We assume, that your container name will be 'test' for this project. You can then build the container with:
`docker build -t test .`
Your container can then be used with test:latest

## Environment Parameters
Docker container environment parameters can be used directly in the YAML file or as external environment file. To demonstrate this, there are two different docker-compose YAML files:
- docker-compose_env_file.yml
This docker-compose file uses the external environment file **parameters.env**.

- docker-compose_inline_parameters.yml
This docker-compose file uses inline definition of all environment parameters.

### Run with Docker-Compose
Choose between the two different YAML files to use external environment file, or inline definition.
`docker-compose -f docker-compose_env_file.yml up`
```console
Recreating test_container ... 
Recreating test_container ... done
Attaching to test_container
test_container | Args: Namespace(optional='optionalParameterFromFile', required='requiredParameterFromFile')
test_container | Starting test...
test_container | Cycle: 0
test_container | Cycle: 1
...
```
`docker-compose -f docker-compose_inline_parameters.yml up`
```console
Recreating test_container ... 
Recreating test_container ... done
Attaching to test_container
test_container | Args: Namespace(optional='optionalParameterCompose', required='requiredParameterCompose')
test_container | Starting test...
test_container | Cycle: 0
test_container | Cycle: 1
...
```

If you rename the YAML file to **docker-compose.yml** you can use the following command:
`docker-compose up`


## Example
How to test the Python script without Docker:
```console
foo@bar:~$ python3 test.py -r Hello -o World
Args: Namespace(optional='World', required='Hello')
Starting test...
Cycle: 0
Cycle: 1
...
```
