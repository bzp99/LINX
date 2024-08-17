out_domain_nl2pandas_examples = {
    1:
    """
task: find one game platform which has one different property compared to all the other platforms
dataset: epic_games
scheme: id, name, game_slug, price, release_date, platform, description, developer, publisher, genres
LDX:
    df = pd.read_csv("epic_games.tsv", delimiter="\t")

    some_platform = df[df['platform'] == <VALUE>]
    other_platform = df[df['platform'] != <VALUE>]

    some_platform_agg = some_platform.groupby(<COL>).agg(<AGG>)
    other_platform_agg = other_platform.groupby(<COL>).agg(<AGG>)
explanation: Split the games to two sets - one with a platform and one with the other platforms.
Then apply the same aggregation on both of them in order to compare them.
""",
    2:
    """
task: investigate what makes data scientists to earn above the 90th percentile salary (above $219,000, according to this dataset) and drill down to a specific reason
dataset: ds_salaries
scheme:	work_year, experience_level, employment_type, job_title, salary, salary_currency, salary_in_usd, employee_residence, remote_ratio, company_location
LDX:
    df = pd.read_csv("ds_salaries.tsv", delimiter="\t")
    greater_than_219000 = df[df['salary_in_usd'] > 219000]
    salaries_properties1 = greater_than_219000.groupby(<COL1>).agg(<AGG1>)
    focus_of_col1 = greater_than_219000[greater_than_219000[<COL1>] == <VALUE1>]
    salaries_properties2 = focus_of_col1.groupby(<COL2>).agg(<AGG2>)
    focus_of_col2 = focus_of_col1[focus_of_col1[<COL2>] == <VALUE2>]
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
    df = pd.read_csv("intel_processors.tsv", delimiter="\t")

    first_product = df[df['Product'] == <VALUE1>]
    second_product = df[df['Product'] == <VALUE2>]
    third_product = df[df['Product'] == <VALUE3>]

    first_product_agg = first_product.groupby(<COL>).agg(<AGG>)
    second_product_agg = second_product.groupby(<COL>).agg(<AGG>)
    third_product_agg = third_product.groupby(<COL>).agg(<AGG>)
explanation: Split the processors to three sets, each one filtered to a different product.
Then apply the same aggregation on each of them in order to compare them.
""",
    4:
    """
task: show the average cost of some two different subsets of houses
dataset: houses
scheme: Area, BHK, Bathroom, Furnishing, Locality, Parking, Price, Status, Transaction, Type, Per_Sqft
LDX:
    df = pd.read_csv("houses.tsv", delimiter="\t")

    first_subset = df[df[<COL1>] == <VALUE1>]
    first_subset_agg = first_subset.groupby(<AGG_COL1>).agg({'Price': 'mean'})

    second_subset = df[df[<COL2] == <VALUE2>]
    second_subset_agg = second_subset.groupby(<AGG_COL2>).agg({'Price': 'mean'})
explanation: filter the houses to some column and some of its values. Then, group the houses according to some column and calculate the average price. Do so one more time but on different subset of the houses.
""",
    5:
    """
task: show two properties of emojis published in 2022 compared to all the emojis
dataset: emojis
scheme: Hex, Rank, Emoji, Year, Category, Subcategory, Name
LDX:
    df = pd.read_csv("emojis.tsv", delimiter="\t")

    emojis_properties_1 = df.groupby(<COL1>).agg(<AGG1>)
    emojis_properties_2 = df.groupby(<COL2>).agg(<AGG2>)

    2022_emojis = df[df['Year'] != '2022']
    2022_emojis_properties1 = 2022_emojis.groupby(<COL1>).agg(<AGG1>)
    2022_emojis_properties2 = 2022_emojis.groupby(<COL2>).agg(<AGG2>)
explanation: Apply two aggregations. Also filter the emojis to those published in the year 2022 and apply the same two aggregations in order to compare it to the previous step.
""",
    6:
    """
task: explore three different car models in different ways
dataset: cars
scheme: addref, city, assembly, body, make, model, year, engine, transmission, fuel
LDX:
       df = pd.read_csv("cars.tsv", delimiter="\t")

       model1 = df[df['model'] == <VALUE1>]
       model2 = df[df['model'] == <VALUE2>]
       model3 = df[df['model'] == <VALUE3>]

       model1_properties = model1.groupby(<COL1>).agg(<AGG1>)
       model2_properties = model2.groupby(<COL2>).agg(<AGG2>)
       model3_properties = model3.groupby(<COL3>).agg(<AGG3>)
explanation: filter to three different flight ids and for each one show some properties.
""",
    8:
    """
task: explore the data, make sure to address two interesting properties of the rapper Drake
dataset: spotify
scheme: Artist, Streams, Daily, As lead, Solo, As feature
LDX:
       df = pd.read_csv("spotify.tsv", delimiter="\t")

       do_some_operations()

       drake_songs = df[df['Artist'] == 'Drake']

       drake_songs_properties_1 = drake_songs.groupby(<COL1>).agg(<AGG1>)
       drake_songs_properties_2 = drake_songs.groupby(<COL2>).agg(<AGG2>)
explanation: At some point, filter artist to Drake at some point. Then, show two different properties using two different group by operations.
""",
    9:
    """
task: show interesting sub-groups of 5-stars repositories
dataset: github
scheme: Name, Description, URL, Created At, Updated At, Homepage, Size, Stars, Forks, Issues
LDX:
        df = pd.read_csv("github.tsv", delimiter="\t")

        5_stars_repos = df[df['Stars'] == '5']

        5_stars_repos_grouped = 5_stars_repos.groupby(<COL1>).agg(<AGG1>)
        5_stars_repos_sub_grouped = 5_stars_repos_grouped.groupby(<COL2>).agg(<AGG2>)
explanation: Filter to repositories with 5 stars.
Then apply some groupby to view it as interesting groups, and apply another groupby to view interesting sub-groups.
"""
}
