    --select driver.* , sessions.session_name
	--from public.driver 
	--inner join public.sessions 
	--on sessions.session_key = driver.session_key



CREATE TABLE IF NOT EXISTS public.driver_historic
(
    ident serial primary key,
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
	time_stamp timestamp NOT NULL,
    
    CONSTRAINT driver_session_fkey FOREIGN KEY (session_key)
        REFERENCES public.sessions (session_key) MATCH FULL
        ON UPDATE RESTRICT
        ON DELETE RESTRICT
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.driver_historic
    OWNER to postgres;


CREATE INDEX IF NOT EXISTS fki_driver_historic_session_fkey
    ON public.driver_historic USING btree
    (session_key ASC NULLS LAST)
    TABLESPACE pg_default;