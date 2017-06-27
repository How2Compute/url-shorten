# Probably the worlst URL shortener...ever
## Written in python/flask!

### Build url-shorten
##### docker build -t url-shorten .

### Run url-shorten
#### Set up a PostgreSQL contianer with the default password of raspberry
##### docker run --name my-postgres -e POSTGRES_PASSWORD=raspberry -d postgres

#### Now use the sql commands/hints in databaseSetup.sql to set up the url-shorten database/table

#### Run the url-shorten container with the minimum of environment variables (DB_HOST)
##### docker run --link my-postgres:postgres -e DB_HOST=postgres -p 8080:8080 url-shorten

### Environment Variables
#### Will follow soonTM!
