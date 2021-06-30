# Getting Started with Python application for performing the following MFA workflows

* [ACCOUNT CREATION]
* [LOGIN]
* [DELETE ACCOUNT]

## Prerequisites

You'll need the following:
* [Python ]
* [FASTAPI]
* [PostgreSQL]

First, you have to install the dependencies listed in the [requirements.txt] to run it locally.

  ```
pip install -r requirements.txt
  ```
## Features

```
* [Full docker Integration ]
* [Prodiuction ready using Uvicorn]
* [Secring password hashing included]
* [JWT token authentication  ]
* [passlib to verify password]
* [PostgreSQL]
* [SwaggerUI]
 ```

## Steps to run the code
1. Clone the repo.
2. Run "docker-compose up --build" command.
3. Open SwaggerUi to access the end points .


## Endpoints
```
* [http://127.0.0.1:8000/docs#/Auth/register_auth_register_post]
* [http://127.0.0.1:8000/docs#/Auth/login_auth_login_post]
* [http://127.0.0.1:8000/docs#/OTPs/send_opt_api_v1_otp_send_post]
* [http://127.0.0.1:8000/docs#/OTPs/verify_opt_api_v1_otp_verify_post ]

 ```