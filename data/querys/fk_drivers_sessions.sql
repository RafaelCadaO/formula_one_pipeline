-- Constraint: driver_session_fkey

-- ALTER TABLE IF EXISTS public.driver DROP CONSTRAINT IF EXISTS driver_session_fkey;

ALTER TABLE IF EXISTS public.driver
    ADD CONSTRAINT driver_session_fkey FOREIGN KEY (session_key)
    REFERENCES public.sessions (session_key) MATCH FULL
    ON UPDATE RESTRICT
    ON DELETE RESTRICT
    NOT VALID;
