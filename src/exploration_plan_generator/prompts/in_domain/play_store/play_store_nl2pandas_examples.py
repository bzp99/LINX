play_store_nl2pandas_examples = {
    1:
    """
task: find one category which has one different property compared to all the other categories

LDX:
    df = pd.read_csv("play_store.tsv", delimiter="\t")

    some_category = df[df['category'] == <VALUE>]
    other_category = df[df['category'] != <VALUE>]

    some_category_agg = some_category.groupby(<COL>).agg(<AGG>)
    other_category_agg = other_category.groupby(<COL>).agg(<AGG>)

explanation: Split the apps to two sets - one with a certain category and one the other categories.
Then apply the same aggregation on both of them in order to compare them.
""",
    2:
    """
task: investigate what makes apps to have more than 1000000 installs and drill down to a specific reason

LDX:
    df = pd.read_csv("play_store.tsv", delimiter="\t")

    1000000_installs_apps = df[df['installs'] > 1000000]

    apps_properties1 = 1000000_installs_apps.groupby(<COL1>).agg(<AGG1>)

    focus_of_col1 = 1000000_installs_apps[1000000_installs_apps[<COL1>] == <VALUE1>]

    apps_properties2 = focus_of_col1.groupby(<COL2>).agg(<AGG2>)

    focus_of_col2 = focus_of_col1[focus_of_col1[<COL2>] == <VALUE2>]

explanation: filter the apps for those with number of installs bigger than 1000000.
Then, group according to some column and apply some aggregation in order to find some column that significantly influences the distribution of those apps.
After that filter on one of the values of the selected column from the previous step. Repeat it once again to drill down more.
""",
    3:
    """
task: compare some three different subsets of content ratings according to some properties

LDX:
    df = pd.read_csv("play_store.tsv", delimiter="\t")

    first_content_rating = df[df['content_rating'] == <VALUE1>]
    second_content_rating = df[df['content_rating'] == <VALUE2>]
    third_content_rating = df[df['content_rating'] == <VALUE3>]

    first_content_rating_agg = first_content_rating.groupby(<COL>).agg(<AGG>)
    second_content_rating_agg = second_content_rating.groupby(<COL>).agg(<AGG>)
    third_content_rating_agg = third_content_rating.groupby(<COL>).agg(<AGG>)

explanation: Split the apps to three sets, each one filtered to a different content rating.
Then apply the same aggregation on each of them in order to compare them.
""",
    4:
    """
task: show the average rating of some two different subsets of apps

LDX:
    df = pd.read_csv("play_store.tsv", delimiter="\t")

    first_subset = df[df[<COL1>] == <VALUE1>]
    first_subset_agg = first_subset.groupby(<AGG_COL1>).agg({'rating': 'mean'})

    second_subset = df[df[<COL2] == <VALUE2>]
    second_subset_agg = second_subset.groupby(<AGG_COL2>).agg({'rating': 'mean'})

explanation: filter the apps to some column and some of its values.
Then, group the apps according to some column and calculate the average rating. Do so one more time but on different subset of the apps.
""",
    5:
    """
task: show two properties of apps with app id 1 compared to all the apps

LDX:
    df = pd.read_csv("play_store.tsv", delimiter="\t")

    apps_properties_1 = df.groupby(<COL1>).agg(<AGG1>)
    apps_properties_2 = df.groupby(<COL2>).agg(<AGG2>)

    appid_apps = apps_df[apps_df['app_id'] == 1]
    appid_apps_properties_1 = appid_apps.groupby(<COL1>).agg(<AGG1>)
    appid_apps_properties_2 = appid_apps.groupby(<COL2>).agg(<AGG2>)

explanation: Apply two aggregations. Also filter the original data to app id 1 and apply the same two aggregations in order to compare it to the previous step.
""",
    6:
    """
task: explore three different app ids in different ways

LDX:
    df = pd.read_csv("play_store.tsv", delimiter="\t")

    category1_apps = df[df['category'] == <VALUE1>]
    category2_apps = df[df['category'] == <VALUE2>]
    category3_apps = df[df['category'] == <VALUE3>]

    category1_apps_properties = category1_apps.groupby(<COL1>).agg(<AGG1>)
    category2_apps_properties = category2_apps.groupby(<COL2>).agg(<AGG2>)
    category3_apps_properties = category3_apps.groupby(<COL3>).agg(<AGG3>)

explanation: filter to three different app categories and for each one show some properties.
""",
    8:
    """
task: explore the data, make sure to address two interesting aspects of Free apps

LDX:
    df = pd.read_csv("play_store.tsv", delimiter="\t")

    do_some_operations()

    free_apps = df[df['type'] == Free]

    free_apps_properties_1 = free_apps.groupby(<COL1>).agg(<AGG1>)
    free_apps_properties_2 = free_apps.groupby(<COL2>).agg(<AGG2>)

explanation: Use descendant in order to filter type to free at some point. Then, show two different properties using two different group by operations.
""",
    9:
    """
task: show interesting sub-groups of apps require 4 Android version

LDX:
    df = pd.read_csv("play_store.tsv", delimiter="\t")

    min_4_version_apps = df[df['min_android_ver'] == '4']

    min_4_version_apps_properties = min_4_version_apps.groupby(<COL1>).agg(<AGG1>)
    min_4_version_apps_sub_properties = min_4_version_apps_properties.groupby(<COL2>).agg(<AGG2>)

explanation: Filter to apps with 4 min android version.
Then apply some groupby to view it as interesting groups, and apply another groupby to view interesting sub-groups.
"""
}