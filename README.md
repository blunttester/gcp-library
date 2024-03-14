# GCP Library

The GCP Library is an open source keyword library designed to simplify automated testing of Google Cloud Platform (GCP) resources. With this library, users can easily create Robot Framework tests to verify the setup and configuration of various GCP resources, including VM instances, Pub/Sub topics, schemas and subscriptions, Dataflow jobs, and BigQuery datasets and tables.

## Features

- **VM Management**: Create, list, and manage VM instances.
- **Pub/Sub Management**: Manage Pub/Sub topics, schemas, and subscriptions.
- **Dataflow Management**: Create and monitor Dataflow jobs.
- **BigQuery Management**: Manage BigQuery datasets and tables.
- Additional features and resources will be added over time.

## Installation

To use the GCP Library, you will need to have Python installed on your machine. Then, you can install the library using pip:

```bash
pip install -e git+https://github.com/yourgithubusername/gcp-library.git#egg=gcp-library
```

Ensure you have the necessary GCP permissions and a service account key to interact with the GCP resources.

## Usage

Before using the library, set up your GCP credentials by exporting the `GOOGLE_APPLICATION_CREDENTIALS` environment variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```

### Example Test Case

Here is an example of a Robot Framework test case for creating and listing VM instances:

```robot
*** Settings ***
Library  GcpLibrary.VMManagement

*** Test Cases ***
Create A VM Instance
    ${operation}=  Create VM Instance  project_id=my-gcp-project  zone=us-central1-a  instance_name=my-instance
    Log  ${operation}

List VM Instances
    @{instances}=  List VM Instances  project_id=my-gcp-project  zone=us-central1-a
    Log  @{instances}
```

## Contributing

We welcome contributions to the GCP Library! If you have suggestions for improvements or new features, please feel free to contribute.

To contribute:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Implement your changes.
4. Write or update tests as necessary.
5. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
