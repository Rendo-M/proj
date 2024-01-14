# Django app with Postgres, Gunicorn, and Nginx in Docker

### Development

Uses the default Django development server.

1. *.env.dev  - env for development
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. *.env.prod* and *.env.prod.db*. - environment variables.
1. Build the images and run the containers:

    ```
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.
