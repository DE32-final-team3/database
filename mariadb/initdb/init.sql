USE tunetalk;

CREATE TABLE user (
    id VARCHAR(255) PRIMARY KEY,
    passwd VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    nickname VARCHAR(255),
    profile VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE track (
    id VARCHAR(255) NOT NULL PRIMARY KEY,
    name VARCHAR(255),
    artist VARCHAR(255),
    image VARCHAR(255),
    acousticness FLOAT,
    danceability FLOAT,
    instrumentalness FLOAT,
    energy FLOAT,
    tempo FLOAT,
    valence FLOAT,
    speechiness FLOAT
);


CREATE TABLE user_playlist (
    user_id VARCHAR(255) NOT NULL,
    track_id VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id, track_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (track_id) REFERENCES track(id)
);


CREATE TABLE user_taste (
    user_id VARCHAR(255) PRIMARY KEY,
    acousticness FLOAT,
    danceability FLOAT,
    instrumentalness FLOAT,
    energy FLOAT,
    tempo FLOAT,
    valence FLOAT,
    speechiness FLOAT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);


CREATE TABLE following (
    following VARCHAR(255) NOT NULL,
    follower VARCHAR(255) NOT NULL,
    PRIMARY KEY (following, follower),
    FOREIGN KEY (following) REFERENCES user(id),
    FOREIGN KEY (follower) REFERENCES user(id)
);
