out_domain_nl2ldx_examples = {
    1:
        """
task: find one game platform which has one different property compared to all the other platforms
dataset: epic_games
scheme: id, name, game_slug, price, release_date, platform, description, developer, publisher, genres
LDX:
      BEGIN CHILDREN {A1,A2}
      A1 LIKE [F,platform,eq,<VALUE>] and CHILDREN {B1}
          B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
      A2 LIKE [F,platform,ne,<VALUE>] and CHILDREN {B2}
          B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
explanation: Split the games to two sets - one with a platform and one with the other platforms.
Then apply the same aggregation on both of them in order to compare them.
""",
    2:
    """
task: investigate what makes data scientists to earn above the 90th percentile salary (above $219,000, according to this dataset) and drill down to a specific reason
dataset: ds_salaries
scheme:	work_year, experience_level, employment_type, job_title, salary, salary_currency, salary_in_usd, employee_residence, remote_ratio, company_location
LDX:
        BEGIN CHILDREN {A1}
        A1 LIKE [F,salary_in_usd,gt,219000] and CHILDREN {B1,B2}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        B2 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {C1,C2}
            C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
            C2 LIKE [F,<COL2>,eq,<VALUE2>]
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
      BEGIN CHILDREN {A1,A2,A3}
      A1 LIKE [F,Product,eq,<VALUE1>] and CHILDREN {B1}
          B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
      A2 LIKE [F,Product,eq,<VALUE2>] and CHILDREN {B2}
          B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
      A3 LIKE [F,Product,eq,<VALUE3>] and CHILDREN {B3}
          B3 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
explanation: Split the processors to three sets, each one filtered to a different product.
Then apply the same aggregation on each of them in order to compare them.
""",
    4:
    """
task: show the average cost of some two different subsets of houses
dataset: houses
scheme: Area, BHK, Bathroom, Furnishing, Locality, Parking, Price, Status, Transaction, Type, Per_Sqft
LDX:
      BEGIN CHILDREN {A1,A2}
      A1 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {B1}
          B1 LIKE [G,<AGG_COL1>,mean,Price]
      A2 LIKE [F,<COL2>,eq,<VALUE2>] and CHILDREN {B2}
          B2 LIKE [G,<AGG_COL2>,mean,Price]
explanation: filter the houses to some column and some of its values. Then, group the houses according to some column and calculate the average price. Do so one more time but on different subset of the houses.
""",
    5:
    """
task: show two properties of emojis published in 2022 compared to all the emojis
dataset: emojis
scheme: Hex, Rank, Emoji, Year, Category, Subcategory, Name
LDX:
      BEGIN CHILDREN {A1,A2,A3}
      A1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
      A2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
      A3 LIKE [F,Year,eq,2022] and CHILDREN {B1,B2}
          B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
          B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
explanation: Apply two aggregations. Also filter the emojis to those published in the year 2022 and apply the same two aggregations in order to compare it to the previous step.
""",
    6:
    """
task: explore three different car models in different ways
dataset: cars
scheme: addref, city, assembly, body, make, model, year, engine, transmission, fuel
LDX:
        BEGIN CHILDREN {A1,A2,A3}
        A1 LIKE [F,model,eq,<VALUE1>] and CHILDREN {B1}
            B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        A2 LIKE [F,model,eq,<VALUE2>] and CHILDREN {B2}
            B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        A3 LIKE [F,model,eq,<VALUE3>] and CHILDREN {B3}
            B3 LIKE [G,<COL3>,<AGG_FUNC3>,<AGG_COL3>]
explanation: filter to three different models and for each one show some properties.
""",
    8:
    """
task: explore the data, make sure to address two interesting properties of the rapper Drake
dataset: spotify
scheme: Artist, Streams, Daily, As lead, Solo, As feature
LDX:
        BEGIN DESCENDANTS {A1}
        A1 LIKE [F,Artist,eq,Drake] and CHILDREN {B1,B2}
            B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
            B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
explanation: Use descendant in order to filter artist to Drake at some point. Then, show two different properties using two different group by operations.
""",
    9:
    """
task: show interesting sub-groups of 5-stars repositories
dataset: github
scheme: Name, Description, URL, Created At, Updated At, Homepage, Size, Stars, Forks, Issues
LDX:
        BEGIN CHILDREN {A1}
        A1 LIKE [F,Stars,eq,5] and CHILDREN {B1}
            B1 LIKE [G,.*] and CHILDREN {C1}
                C1 LIKE [G,.*]
explanation: Filter to repositories with 5 stars.
Then apply some groupby to view it as interesting groups, and apply another groupby to view interesting sub-groups.
"""
}