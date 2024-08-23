out_domain_sql2ldx_examples = {
    1:
        """
SQL:
    SELECT <COL>,<AGG>
    FROM epic_games
    WHERE platform = <VALUE>
    GROUP BY <COL>;
    
    SELECT <COL>,<AGG>
    FROM epic_games
    WHERE platform != <VALUE>
    GROUP BY <COL>;
    
LDX:
      BEGIN CHILDREN {A1,A2}
      A1 LIKE [F,platform,eq,<VALUE>] and CHILDREN {B1}
          B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
      A2 LIKE [F,platform,ne,<VALUE>] and CHILDREN {B2}
          B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    """,
    2:
        """
SQL:
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
    
LDX:
        BEGIN CHILDREN {A1}
        A1 LIKE [F,salary_in_usd,gt,219000] and CHILDREN {B1,B2}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        B2 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {C1,C2}
            C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
            C2 LIKE [F,<COL2>,eq,<VALUE2>]
    """,
    3:
        """
SQL:
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

LDX:
      BEGIN CHILDREN {A1,A2,A3}
      A1 LIKE [F,Product,eq,<VALUE1>] and CHILDREN {B1}
          B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
      A2 LIKE [F,Product,eq,<VALUE2>] and CHILDREN {B2}
          B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
      A3 LIKE [F,Product,eq,<VALUE3>] and CHILDREN {B3}
          B3 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    """,
    4:
        """
SQL:       
    SELECT <AGG_COL1>,AVG(Price)
    FROM houses
    WHERE <COL1> = <VALUE1>
    GROUP BY <AGG_COL1>;
    
    SELECT <AGG_COL2>,AVG(Price)
    FROM houses
    WHERE <COL2> = <VALUE2>
    GROUP BY <AGG_COL2>;
    
LDX:
      BEGIN CHILDREN {A1,A2}
      A1 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {B1}
          B1 LIKE [G,<AGG_COL1>,mean,Price]
      A2 LIKE [F,<COL2>,eq,<VALUE2>] and CHILDREN {B2}
          B2 LIKE [G,<AGG_COL2>,mean,Price]
    """,
    5:
        """
SQL:       
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
    
LDX:
      BEGIN CHILDREN {A1,A2,A3}
      A1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
      A2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
      A3 LIKE [F,Year,eq,2022] and CHILDREN {B1,B2}
          B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
          B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    """,
    6:
        """
SQL:       
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
    
LDX:
        BEGIN CHILDREN {A1,A2,A3}
        A1 LIKE [F,model,eq,<VALUE1>] and CHILDREN {B1}
            B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        A2 LIKE [F,model,eq,<VALUE2>] and CHILDREN {B2}
            B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        A3 LIKE [F,model,eq,<VALUE3>] and CHILDREN {B3}
            B3 LIKE [G,<COL3>,<AGG_FUNC3>,<AGG_COL3>]
    """,
    8:
        """
SQL:       
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
    
LDX:
        BEGIN DESCENDANTS {A1}
        A1 LIKE [F,Artist,eq,Drake] and CHILDREN {B1,B2}
            B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
            B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    """,
    9:
        """
SQL:       
    SELECT <COL1>,<COL2>,<AGG1>,<AGG2>
    FROM github
    WHERE Stars = 5
    GROUP BY <COL1>,<COL2>;
LDX:
        BEGIN CHILDREN {A1}
        A1 LIKE [F,Stars,eq,5] and CHILDREN {B1}
            B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>] and CHILDREN {C1}
                C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    """
}