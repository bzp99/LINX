out_domain_nl2sql_examples = {
    1:
        """
task: find one game platform which has one different property compared to all the other platforms
dataset: epic_games
scheme: id, name, game_slug, price, release_date, platform, description, developer, publisher, genres
LDX:
    SELECT <COL>,<AGG>
    FROM epic_games
    WHERE platform = <VALUE>
    GROUP BY <COL>;
    
    SELECT <COL>,<AGG>
    FROM epic_games
    WHERE platform != <VALUE>
    GROUP BY <COL>;
explanation: Split the games to two sets - one with a platform and one with the other platforms.
Then apply the same aggregation on both of them in order to compare them.
""",
    2:
    """
task: investigate what makes data scientists to earn above the 90th percentile salary (above $219,000, according to this dataset) and drill down to a specific reason
dataset: ds_salaries
scheme:	work_year, experience_level, employment_type, job_title, salary, salary_currency, salary_in_usd, employee_residence, remote_ratio, company_location
LDX:        
    high_salaries AS (
        SELECT *
        FROM ds_salaries
        WHERE salary_in_usd > 219000
    ),
    
    SELECT <COL1>, <AGG1>
    FROM high_salaries
    GROUP BY <COL1>
    
    focus_of_col1 AS (
        SELECT *
        FROM high_salaries
        WHERE <COL1> = <VALUE1>
    ),
    
    SELECT <COL2>, <AGG_FUNC2> 
    FROM focus_of_col1
    GROUP BY <COL2>
    
    SELECT *
    FROM focus_of_col1
    WHERE <COL2> = <VALUE2>

explanation: filter to salaries in usd greater than 219000.
Then, group according to some column and apply some aggregation in order to find some column that significantly influences the distribution of them.
After that filter on one of the values of the selected column from the previous step. Repeat it once again to drill down more.
""",
    3:
    """
task: compare some three different subsets of processors according to some properties
dataset: intel_processors
scheme:	Product, Status, Release Date, Cores, Threads, Lithography, Max. Turbo Freq, Base Freq, TDP, Cache
LDX:          
    SELECT <COL>,<AGG>
    FROM intel_processors
    WHERE Product = <VALUE1>
    GROUP BY <COL>;
    
    SELECT <COL>,<AGG>
    FROM intel_processors
    WHERE Product = <VALUE2>
    GROUP BY <COL>;
    
    SELECT <COL>,<AGG>
    FROM intel_processors
    WHERE Product = <VALUE3>
    GROUP BY <COL>;        
explanation: Split the processors to three sets, each one filtered to a different product.
Then apply the same aggregation on each of them in order to compare them.
""",
    4:
    """
task: show the average cost of some two different subsets of houses
dataset: houses
scheme: Area, BHK, Bathroom, Furnishing, Locality, Parking, Price, Status, Transaction, Type, Per_Sqft
LDX:
    SELECT <AGG_COL1>,AVG(Price)
    FROM houses
    WHERE <COL1> = <VALUE1>
    GROUP BY <AGG_COL1>;
    
    SELECT <AGG_COL2>,AVG(Price)
    FROM houses
    WHERE <COL2> = <VALUE2>
    GROUP BY <AGG_COL2>;
explanation: filter the houses to some column and some of its values. Then, group the houses according to some column and calculate the average price. Do so one more time but on different subset of the houses.
""",
    5:
    """
task: show two properties of emojis published in 2022 compared to all the emojis
dataset: emojis
scheme: Hex, Rank, Emoji, Year, Category, Subcategory, Name
LDX:
    SELECT <AGG_COL1>,<AGG1>
    FROM emojis
    GROUP BY <AGG_COL1>;
    
    SELECT <AGG_COL2>,<AGG2>
    FROM emojis
    GROUP BY <AGG_COL2>;
    
    2022_emojis as (SELECT *
    FROM emojis
    WHERE Year == 2022);
    
    SELECT <AGG_COL1>,<AGG1>
    FROM 2022_emojis
    GROUP BY <AGG_COL1>;
    
    SELECT <AGG_COL2>,<AGG2>
    FROM 2022_emojis
    GROUP BY <AGG_COL2>;
explanation: Apply two aggregations. Also filter the emojis to those published in the year 2022 and apply the same two aggregations in order to compare it to the previous step.
""",
    6:
    """
task: explore three different car models in different ways
dataset: cars
scheme: addref, city, assembly, body, make, model, year, engine, transmission, fuel
LDX:
    SELECT <COL1>,<AGG1>
    FROM cars
    WHERE model = <VALUE1>
    GROUP BY <COL1>;
    
    SELECT <COL2>,<AGG2>
    FROM cars
    WHERE model = <VALUE2>
    GROUP BY <COL2>;
    
    SELECT <COL3>,<AGG3>
    FROM cars
    WHERE model = <VALUE3>
    GROUP BY <COL3>;
explanation: filter to three different models and for each one show some properties.
""",
    8:
    """
task: explore the data, make sure to address two interesting properties of the rapper Drake
dataset: spotify
scheme: Artist, Streams, Daily, As lead, Solo, As feature
LDX:
    -- do some queries before

    drake_songs as (SELECT *
    FROM spotify
    WHERE Artist = Drake);
    
    SELECT <AGG_COL1>,<AGG1>
    FROM drake_songs
    GROUP BY <AGG_COL1>;
    
    SELECT <AGG_COL2>,<AGG2>
    FROM drake_songs
    GROUP BY <AGG_COL2>;
explanation: Use descendant in order to filter artist to Drake at some point. Then, show two different properties using two different group by operations.
""",
    9:
    """
task: show interesting sub-groups of 5-stars repositories
dataset: github
scheme: Name, Description, URL, Created At, Updated At, Homepage, Size, Stars, Forks, Issues
LDX:   
    SELECT <COL1>,<COL2>,<AGG1>,<AGG2>
    FROM github
    WHERE Stars = 5
    GROUP BY <COL1>,<COL2>;
explanation: Filter to repositories with 5 stars.
Then apply some groupby to view it as interesting groups, and apply another groupby to view interesting sub-groups.
"""
}