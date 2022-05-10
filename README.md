![dev integration]({YOUR_REPO_HERE}/actions/workflows/continuous-integration-dev.yml/badge.svg)
![qa integration]({YOUR_REPO_HERE}/actions/workflows/continuous-integration-staging.yml/badge.svg)
![prod integration]({YOUR_REPO_HERE}/actions/workflows/continuous-integration-master.yml/badge.svg)
![dev deployment]({YOUR_REPO_HERE}/actions/workflows/continuous-deployment-dev.yml/badge.svg)
![qa deployment]({YOUR_REPO_HERE}/actions/workflows/continuous-deployment-staging.yml/badge.svg)
![prod deployment]({YOUR_REPO_HERE}/actions/workflows/continuous-deployment-master.yml/badge.svg)

# Python Serverless template

1. [Description](#description)
2. [Instructions](#instructions)
3. [Local DynamoDB settings](#local-dynamodb-settings)

<a name="description"></a>

## 1. Description

This is a **template** project that allow developers to quickly create a Python Serverless project.

This template includes by default:

- **Local Serverless framework support**. (Using then command: `yarn local`)
- **Local DynamoDB support**. (Using then command: `yarn local`)
- **Test support using pytest**. (Using the command: `pytest`)
- **CI/CD pipeline** for dev, staging and master branches. (Check the .github/workflows/ directories)

The directories structure is as follows:

- **test/:** All service's tests must be placed under this directory. Tests can be written in TypeScript.
- **src/handler:** All the handler classes. All handler should be methods from a class in this directory.
- **src/model:** The model regarding the service should be placed here.
- **src/service:** All services including custom services and services related to AWS should be placed here. This includes
  for example, DynamoDB service, or a custom service for your domain.
- **src/serverless:** In this directory, it should be placed everything regarding Serverless framework. This includes plugins
  files (`src/serverless/plugins`) or Cloud Formation resources .yml files (`src/serverless/resources`) to include in the main
  `serverless.yml`.

<a name="instructions"></a>

## 2. Instructions

1. Go to `package.json` file and update the `repository`, `name`, `description` and `main` fields.
2. Go to `serverless.yml` file and update `custom.service` field.
3. Remove the .git folder placed at the root of the project.
4. Execute `git init` at the root of the project to create a new git repository.
5. Execute `yarn install` to install all the dependencies.
6. Execute `virtualenv -p python3 venv` to create a Virtual Environment (Need to use Python 3.9)
7. Execute `source venv/bin/activate` to activate the Virtual Environment
8. Add your dependencies on the `requirements.txt` file
9. Execute `pip install -r requirements.txt` to install all the dependencies
8. Execute `yarn local` to run the service locally.
9. Develop new code and enjoy...

Finally, it is recommended to copy this README file somewhere else and update this one so that ir reflects the right README
for the service to develop.

<a name="local-dynamodb-settings"></a>

## 3. Local DynamoDB settings

By default, this template will migrate the local DynamoDB using the table's description declared under the `Resources`
section in the `serverless.yml` file.

It uses a file under `src/serverless/plugins/localDynamoDB` to seed the local DynamoDB.

To seed new tables, just add under the `src/serverless/plugins/localDynamoDB` directory a new .json file and add a new entry
under `seed.domain.sources` in `serverless.yml`.
