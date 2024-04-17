netflix_nl2pandas_examples = {
    1:
    """
task: find one rating which has one different property compared to all the other show ids

LDX:
    df = pd.read_csv("netflix.tsv", delimiter="\t")

    some_rating = df[df['rating'] == <VALUE>]
    other_rating = df[df['rating'] != <VALUE>]

    some_rating_agg = some_rating.groupby(<COL>).agg(<AGG>)
    other_rating_agg = other_rating.groupby(<COL>).agg(<AGG>)

explanation: Split the tv shows to two sets - one with a certain rating and one with the other ratings.
Then apply the same aggregation on both of them in order to compare them.
""",
    2:
    """
task: investigate what makes shows to be directed by Christopher Nolan and drill down to a specific reason

LDX:
    df = pd.read_csv("netflix.tsv", delimiter="\t")

    christopher_nolan_shows = df[df['director'] == 'Christopher Nolan']

    shows_properties1 = christopher_nolan_shows.groupby(<COL1>).agg(<AGG1>)

    focus_of_col1 = christopher_nolan_shows[christopher_nolan_shows[<COL1>] == <VALUE1>]

    shows_properties2 = focus_of_col1.groupby(<COL2>).agg(<AGG2>)

    focus_of_col2 = focus_of_col1[focus_of_col1[<COL2>] == <VALUE2>]

explanation: filter the shows to those directed by Christopher Nolan.
Then, group according to some column and apply some aggregation in order to find some column that significantly influences the distribution of those shows.
After that filter on one of the values of the selected column from the previous step. Repeat it once again to drill down more.
""",
    3:
    """
task: compare some three different subsets of directors according to some properties

LDX:
    df = pd.read_csv("netflix.tsv", delimiter="\t")

    first_director = df[df['director'] == <VALUE1>]
    second_director = df[df['director'] == <VALUE2>]
    third_director = df[df['director'] == <VALUE3>]

    first_director_agg = first_director.groupby(<COL>).agg(<AGG>)
    second_director_agg = second_director.groupby(<COL>).agg(<AGG>)
    third_director_agg = third_director.groupby(<COL>).agg(<AGG>)

explanation: Split the shows to three sets, each one filtered to a different director.
Then apply the same aggregation on each of them in order to compare them.
""",
    4:
    """
task: show the average duration of some two different subsets of shows

LDX:
    df = pd.read_csv("netflix.tsv", delimiter="\t")

    first_subset = df[df[<COL1>] == <VALUE1>]
    first_subset_agg = first_subset.groupby(<AGG_COL1>).agg({'duration': 'mean'})

    second_subset = df[df[<COL2] == <VALUE2>]
    second_subset_agg = second_subset.groupby(<AGG_COL2>).agg({'duration': 'mean'})

explanation: filter the shows to some column and some of its values.
Then, group the shows according to some column and calculate the average duration. Do so one more time but on different subset of the shows.
""",
    5:
    """
task: show two properties of the show "Hero" compared to all the shows

LDX:
    df = pd.read_csv("netflix.tsv", delimiter="\t")

    shows_properties_1 = df.groupby(<COL1>).agg(<AGG1>)
    shows_properties_2 = df.groupby(<COL2>).agg(<AGG2>)

    hero_shows = df['Hero' in df['title']]
    hero_shows_properties_1 = hero_shows.groupby(<COL1>).agg(<AGG1>)
    hero_shows_properties_2 = hero_shows.groupby(<COL2>).agg(<AGG2>)

explanation: Apply two aggregations. Also filter to shows with title contains "Hero" and apply the same two aggregations in order to compare it to the previous step.
""",
    6:
    """
task: explore three different release years in different ways

LDX:
    df = pd.read_csv("netflix.tsv", delimiter="\t")

    release_year1_shows = df[df['release_year'] == <VALUE1>]
    release_year2_shows = df[df['release_year'] == <VALUE2>]
    release_year3_shows = df[df['release_year'] == <VALUE3>]

    release_year1_shows_properties = release_year1_shows.groupby(<COL1>).agg(<AGG1>)
    release_year2_shows_properties = release_year2_shows.groupby(<COL2>).agg(<AGG2>)
    release_year3_shows_properties = release_year3_shows.groupby(<COL3>).agg(<AGG3>)

explanation: filter to three different release years and for each one show some properties.
""",
    8:
    """
task: explore the data, make sure to address two interesting aspects of shows with rating TV-14

LDX:
    df = pd.read_csv("netflix.tsv", delimiter="\t")

    do_some_operations()

    tv_14_shows = df[df['rating'] == 'TV-14']

    tv_14_shows_properties1 = tv_14_shows.groupby(<COL1>).agg(<AGG1>)
    tv_14_shows_properties2 = tv_14_shows.groupby(<COL2>).agg(<AGG2>)

explanation: Use descendant in order to filter rating to TV-14 at some point. Then, show two different properties using two different group by operations.
""",
    9:
    """
task: show interesting sub-groups of shows filmed in Israel

LDX:
    df = pd.read_csv("netflix.tsv", delimiter="\t")

    israel_shows = df[df['country'] == 'Israel']

    israel_shows_properties = israel_shows.groupby(<COL1>).agg(<AGG1>)
    israel_shows_sub_properties = israel_shows_properties.groupby(<COL2>).agg(<AGG2>)

explanation: Filter to shows filmed in Israel.
Then apply some groupby to view it as interesting groups, and apply another different groupby to view interesting sub-groups.
"""
}