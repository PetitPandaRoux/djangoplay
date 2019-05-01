'''
CREATE DATABASE db_play;

CREATE USER play WITH PASSWORD 'playtimewithdjangoprojects';

ALTER ROLE play SET client_encoding To 'utf8';

ALTER ROLE play SET default_transaction_isolation TO 'read committed';

-- pas nécessaire

-- ALTER ROLE play SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE db_play TO play;
'''

