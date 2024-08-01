CREATE OR REPLACE PROCEDURE load_driver_data_from_csv(p_csv_path VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Truncate the table
    TRUNCATE TABLE public.driver;
    
    -- Load data from the CSV file
    EXECUTE format('COPY public.driver FROM %L WITH (FORMAT csv, HEADER true)', p_csv_path);
END;
$$;
