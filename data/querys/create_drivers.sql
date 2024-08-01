-- Table: public.driver

-- DROP TABLE IF EXISTS public.driver;

CREATE TABLE IF NOT EXISTS public.driver
(
    session_key integer NOT NULL,
    meeting_key integer NOT NULL,
    broadcast_name character varying(60) COLLATE pg_catalog."default" NOT NULL,
    country_code character varying(10) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(20) COLLATE pg_catalog."default" NOT NULL,
    full_name character varying(60) COLLATE pg_catalog."default" NOT NULL,
    headshot_url character varying(200) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(60) COLLATE pg_catalog."default" NOT NULL,
    driver_number integer NOT NULL,
    team_colour character varying(10) COLLATE pg_catalog."default" NOT NULL,
    team_name character varying(60) COLLATE pg_catalog."default" NOT NULL,
    name_acronym character varying(5) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT driver_pkey PRIMARY KEY (driver_number)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.driver
    OWNER to postgres;