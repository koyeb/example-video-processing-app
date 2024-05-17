<div align="center">
  <a href="https://koyeb.com">
    <img src="https://www.koyeb.com/static/images/icons/koyeb.svg" alt="Logo" width="80" height="80">
  </a>
  <h3 align="center">Koyeb Serverless Platform</h3>
  <p align="center">
    Deploy a video processing pipeline app on Koyeb
    <br />
    <a href="https://koyeb.com">Learn more about Koyeb</a>
    ·
    <a href="https://koyeb.com/docs">Explore the documentation</a>
    ·
    <a href="https://koyeb.com/tutorials">Discover our tutorials</a>
  </p>
</div>


## About Koyeb and the video processing pipeline example application

Koyeb is a developer-friendly serverless platform to deploy apps globally. No-ops, servers, or infrastructure management.  This repository contains a job search application you can deploy on the Koyeb serverless platform for testing.

This example application, when deployed alongside  its companion [video processing worker service](https://github.com/koyeb/example-video-processing-worker), allows you to upload videos that will be automatically tagged and categorized by AssemblyAI.  This repository is the web application built in Django.  It allows users to upload videos and play uploaded content.  During the upload, videos are passed to the worker service for tagging and categorization.

## Getting Started

Follow the steps below to deploy and run the example video processing pipeline application on your Koyeb account.

### Requirements

* A [Koyeb account](https://app.koyeb.com/auth/signup) to build, deploy, and run this application.
* A web-accessible PostgreSQL database to store content.  You can use [Koyeb's PostgreSQL databases](https://www.koyeb.com/docs/databases) to fulfill this requirement.

### Deploy using the Koyeb button

Once you have a PostgreSQL database deployed, you can deploy the video processing web app.  In the [Koyeb Control Panel](https://app.koyeb.com), on the **Overview** tab, click the **Create Web Service** button to begin:

1. Select **GitHub** as the deployment method.
2. Select your project repository if you forked this repository.  Alternatively, enter `https://github.com/koyeb/example-video-processing-app` in the **Public GitHub repository** field to use this repository as-is.
3. In the **Builder** section, override the **Run command** with `python manage.py runserver 0.0.0.0:8000`.
4. In the **App and Service names** section, configure the **App name**. This will impact the environment variable values you define next.
5. In the **Environment variables** section, click **Bulk edit** to enter multiple environment variables at once. In the text box that appears, paste the following:
    ```
    DJANGO_DB_HOST=
    DJANGO_DB_USER=
    DJANGO_DB_PASSWORD=
    DJANGO_DB_NAME=
    ALLOWED_HOSTS=
    CSRF_TRUSTED_ORIGINS=
    DOMAIN=
    DJANGO_SECRET_KEY=
    WORKER_URL=
    ```

    Fill in the variables as follows:

    * `DJANGO_DB_HOST`: The hostname of the PostgreSQL database.
    * `DJANGO_DB_USER`: The PostgreSQL username to authenticate with.
    * `DJANGO_DB_PASSWORD`: The PostgreSQL password to authenticate with.
    * `DJANGO_DB_NAME`: The name of the PostgreSQL database to connect to.
    * `ALLOWED_HOSTS`: The bare hostname where this application will be deployed (without `https://`).
    * `CSRF_TRUSTED_ORIGINS`: The domain where this application will be deployed (with `https://`).
    * `DOMAIN`: The domain where this application will be deployed (with `https://`).
    * `DJANGO_SECRET_KEY`: A secret key used for encryption by Django.  If you have Django installed locally, you can generate one by typing: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    `.
    * `WORKER_URL`: The URL where the [worker service](https://github.com/koyeb/example-video-processing-worker) will be deployed (with `https://`).

5. Click **Deploy**.

Once the web application is up and running, you can deploy the [worker service](https://github.com/koyeb/example-video-processing-worker) responsible for processing videos.

## Contributing

If you have any questions, ideas or suggestions regarding this application sample, feel free to open an [issue](https://github.com/koyeb/example-video-processing-app/issues) or fork this repository and open a [pull request](https://github.com/koyeb/example-video-processing-app/pulls).

## Contact

[Koyeb](https://www.koyeb.com) - [@gokoyeb](https://twitter.com/gokoyeb) - [Slack](http://slack.koyeb.com/)
