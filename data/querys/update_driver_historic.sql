-- PROCEDURE: public.update_driver_historic()

-- DROP PROCEDURE IF EXISTS public.update_driver_historic();

CREATE OR REPLACE PROCEDURE public.update_driver_historic(
	)
LANGUAGE 'plpgsql'
AS $BODY$
begin

	insert into public.driver_historic(
        session_key, 
        meeting_key, 
        broadcast_name, 
        country_code, 
        first_name, 
        full_name, 
        headshot_url, 
        last_name, 
        driver_number, 
        team_colour, 
        team_name, 
        name_acronym,
        time_stamp
    )
	SELECT 
	session_key, 
	meeting_key, 
	broadcast_name, 
	country_code, 
	first_name, 
	full_name, 
	headshot_url, 
	last_name, 
	driver_number, 
	team_colour, 
	team_name, 
	name_acronym,
	now()
	from public.driver;

end;
$BODY$;
ALTER PROCEDURE public.update_driver_historic()
    OWNER TO postgres;
