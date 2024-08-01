-- Table: public.driver

-- DROP TABLE IF EXISTS public.driver;

CREATE TABLE IF NOT EXISTS public.sessions
(
    session_key integer NOT NULL,
    session_name integer NOT NULL,
    date_start TIMESTAMPTZ NOT NULL,
	date_end	TIMESTAMPTZ NOT NULL,
	gmt_offset	TIME NOT NULL,
	session_type VARCHAR (10) NOT NULL,	
	meeting_key	INT NOT NULL,
	location	VARCHAR (60),
	country_key	INT NOT NULL,
	country_code	VARCHAR (4) NOT NULL,
	country_name	VARCHAR(25)NOT NULL,
	circuit_key	SMALLINT NOT NULL,
	circuit_short_name	VARCHAR(60) NOT NULL,
	year INT NOT NULL,
   
    CONSTRAINT session_pkey PRIMARY KEY (session_key)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sessions
    OWNER to postgres;