/* A database to contain previously queried webscrapes */
PRAGMA foreign_keys=off;
BEGIN TRANSACTION;

Create Table prev_queries (
    link TEXT,
    string TEXT,
    tag TEXT
);

COMMIT;
