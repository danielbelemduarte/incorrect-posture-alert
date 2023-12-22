CREATE USER posture;

CREATE DATABASE posture;
GRANT ALL PRIVILEGES ON DATABASE posture TO posture;

CREATE TABLE posture_logs (
	id serial PRIMARY KEY,
	posture_image_description VARCHAR(255) UNIQUE NOT NULL,
    posture_result  VARCHAR(3) UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
);