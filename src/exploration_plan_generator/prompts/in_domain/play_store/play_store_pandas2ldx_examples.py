play_store_pandas2ldx_examples = {
    1:
        """
Pandas:
    df = pd.read_csv("play_store.tsv", delimiter="\\t")

    some_category = df[df['category'] == <VALUE>]
    other_category = df[df['category'] != <VALUE>]

    some_category_agg = some_category.groupby(<COL>).agg(<AGG>)
    other_category_agg = other_category.groupby(<COL>).agg(<AGG>)

    # compare the two aggregations
    comparison = pd.concat([some_category_agg, other_category_agg], axis=1)
LDX:
    BEGIN CHILDREN {A1,A2}
    A1 LIKE [F,category,eq,<VALUE>] and CHILDREN {B1}
      B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A2 LIKE [F,category,ne,<VALUE>] and CHILDREN {B2}
      B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. some_category and other_category are both using df, so they are converted to two children A1,A2 of df corresponding node which is BEGIN.
3. some_category_agg is using some_category, so it would be a node of A1, naming it B1.
4. other_category_agg is using other_rating, so it would be a node of A2, naming it B2.
5. concatination isn't supported (only filter and groupby are supported), therefore the last pandas line is ignored.
""",
    2:
        """
Pandas:
    df = pd.read_csv("play_store.tsv", delimiter="\\t")

    1000000_installs_apps = df[df['installs'] > 1000000]

    apps_properties1 = 1000000_installs_apps.groupby(<COL1>).agg(<AGG1>)

    focus_of_col1 = 1000000_installs_apps[1000000_installs_apps[<COL1>] == <VALUE1>]

    apps_properties2 = focus_of_col1.groupby(<COL2>).agg(<AGG2>)

    focus_of_col2 = focus_of_col1[focus_of_col1[<COL2>] == <VALUE2>]
LDX:
    BEGIN CHILDREN {A1}
    A1 LIKE [F,installs,gt,1000000] and CHILDREN {B1,B2}
    B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    B2 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {C1,C2}
        C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        C2 LIKE [F,<COL2>,eq,<VALUE2>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. 1000000_installs_apps is using df, so it's converted to child A1 of df corresponding node, which is BEGIN.
3. apps_properties1 is using 1000000_installs_apps, so it would be a node of A1, naming it B1.
4. focus_of_col1 is also using 1000000_installs_apps, so it would be another node of A1, naming it B2.
5. apps_properties2 is using focus_of_col1, so it would be a node of B2, naming it C1.
6. focus_of_col2 is also using focus_of_col1, so it would be another node of B2, naming it C2.
    """,
    3:
        """
    Pandas:
        df = pd.read_csv("play_store.tsv", delimiter="\\t")
    
        first_content_rating = df[df['content_rating'] == <VALUE1>]
        second_content_rating = df[df['content_rating'] == <VALUE2>]
        third_content_rating = df[df['content_rating'] == <VALUE3>]
    
        first_content_rating_agg = first_content_rating.groupby(<COL>).agg(<AGG>)
        second_content_rating_agg = second_content_rating.groupby(<COL>).agg(<AGG>)
        third_content_rating_agg = third_content_rating.groupby(<COL>).agg(<AGG>)
    LDX:
        BEGIN CHILDREN {A1,A2,A3}
        A1 LIKE [F,content_rating,eq,<VALUE1>] and CHILDREN {B1}
          B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
        A2 LIKE [F,content_rating,eq,<VALUE2>] and CHILDREN {B2}
          B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
        A3 LIKE [F,content_rating,eq,<VALUE3>] and CHILDREN {B3}
          B3 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    explanation:
    1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
    2. first_content_rating, second_content_rating and third_content_rating are using df, so they are converted to a three children A1,A2,A3 of df corresponding node, which is BEGIN.
    3. first_content_rating_agg is using first_content_rating, so it would be child of A1, naming it B1.
    4. second_content_rating_agg is using second_content_rating, so it would be child of A2, naming it B2.
    5. third_content_rating_agg is using third_content_rating, so it would be child of A3, naming it B3.
        """,
    4:
        """
    Pandas:
        df = pd.read_csv("play_store.tsv", delimiter="\\t")
    
        first_subset = df[df[<COL1>] == <VALUE1>]
        first_subset_agg = first_subset.groupby(<AGG_COL1>).agg({'rating': 'mean'})
    
        second_subset = df[df[<COL2] == <VALUE2>]
        second_subset_agg = second_subset.groupby(<AGG_COL2>).agg({'rating': 'mean'})
    
        highest_rating = max(first_subset_agg['rating'], second_subset_agg['rating'])
    LDX:
        BEGIN CHILDREN {A1,A2}
        A1 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {B1}
          B1 LIKE [G,<AGG_COL1>,mean,rating]
        A2 LIKE [F,<COL2>,eq,<VALUE2>] and CHILDREN {B2}
          B2 LIKE [G,<AGG_COL2>,mean,rating]
    explanation:
    1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
    2. first_subset is using df, so it's converted to a child A1 of df corresponding node, which is BEGIN.
    3. first_subset_agg is using first_subset, so it would be child of A1, naming it B1.
    4. second_subset is also using df, so it's converted to another child A2 of df corresponding node, which is BEGIN.
    5. second_subset_agg is using second_subset, so it would be child of A2, naming it B2.
    6. max isn't a supported operation (only filter and groupby are supported) so the corresponding line is ignored.
        """,
    5:
        """
    Pandas:
        df = pd.read_csv("play_store.tsv", delimiter="\\t")
    
        apps_properties_1 = df.groupby(<COL1>).agg(<AGG1>)
        apps_properties_2 = df.groupby(<COL2>).agg(<AGG2>)
    
        appid_apps = df[df['app_id'] == 1]
        appid_apps_properties_1 = appid_apps.groupby(<COL1>).agg(<AGG1>)
        appid_apps_properties_2 = appid_apps.groupby(<COL2>).agg(<AGG2>)
    LDX:
        BEGIN CHILDREN {A1,A2,A3}
        A1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        A2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        A3 LIKE [F,app_id,eq,1] and CHILDREN {B1,B2}
          B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
          B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    explanation:
    1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
    2. apps_properties_1 and apps_properties_2 are both using df, so they are converted to two children A1,A2 of df corresponding node which is BEGIN.
    3. appid_apps is also using df, so it would be another node of BEGIN, naming it A3.
    4. appid_apps_properties_1 and appid_apps_properties_2 are using appid_apps, so they are converted to children of A3, naming them B1,B2.
        """,
    6:
        """
    Pandas:
        df = pd.read_csv("play_store.tsv", delimiter="\\t")
    
        category1_apps = df[df['category'] == <VALUE1>]
        category2_apps = df[df['category'] == <VALUE2>]
        category3_apps = df[df['category'] == <VALUE3>]
    
        category1_apps_properties = category1_apps.groupby(<COL1>).agg(<AGG1>)
        category2_apps_properties = category2_apps.groupby(<COL2>).agg(<AGG2>)
        category3_apps_properties = category3_apps.groupby(<COL3>).agg(<AGG3>)
    LDX:
        BEGIN CHILDREN {A1,A2,A3}
        A1 LIKE [F,category,eq,<VALUE1>] and CHILDREN {B1}
            B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        A2 LIKE [F,category,eq,<VALUE2>] and CHILDREN {B2}
            B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        A3 LIKE [F,category,eq,<VALUE3>] and CHILDREN {B3}
            B3 LIKE [G,<COL3>,<AGG_FUNC3>,<AGG_COL3>]
    explanation:
    1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
    2. category1_apps, category2_apps and category3_apps are using df, so they are converted to three children A1,A2,A3 of df corresponding node, which is BEGIN.
    3. category1_apps_properties is using category1_apps, so it would be a child A1, naming it B1.
    4. category2_apps_properties is using category2_apps, so it would be a child A2, naming it B2.
    5. category3_apps_properties is using category3_apps, so it would be a child A3, naming it B3.
        """,
    8:
        """
    Pandas:
        df = pd.read_csv("play_store.tsv", delimiter="\\t")
    
        do_some_operations()
    
        free_apps = df[df['type'] == Free]
    
        free_apps_properties_1 = free_apps.groupby(<COL1>).agg(<AGG1>)
        free_apps_properties_2 = free_apps.groupby(<COL2>).agg(<AGG2>)
    LDX:
        BEGIN DESCENDANTS {A1}
        A1 LIKE [F,type,eq,Free] and CHILDREN {B1,B2}
            B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
            B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    explanation:
    1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
    2. do_some_operations() indicates that the next operation would be converted to a descendant and not a direct child, since there are some operations applied between the two.
    3. free_apps is using df, so it would a be a descendant of df corresponding node, which is BEGIN.
    4. free_apps_properties_1, free_apps_properties_2 are using free_apps, so they would be two children of A1, naming them B1,B2 respectively.
        """,
    9:
        """
   Pandas:
       df = pd.read_csv("play_store.tsv", delimiter="\\t")
   
       min_4_version_apps = df[df['min_android_ver'] == '4']
   
       min_4_version_apps_properties = min_4_version_apps.groupby(<COL1>).agg(<AGG1>)
       min_4_version_apps_sub_properties = min_4_version_apps_properties.groupby(<COL2>).agg(<AGG2>)
   LDX:
       BEGIN CHILDREN {A1}
       A1 LIKE [F,min_android_ver,eq,4] and CHILDREN {B1}
           B1 LIKE [G,.*] and CHILDREN {C1}
               C1 LIKE [G,.*]
   explanation:
   1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
   2. min_4_version_apps is using df, so it would a be a child of df corresponding node, which is BEGIN.
   3. min_4_version_apps_properties is using min_4_version_apps, so it would a child of A1, naming it B1.
   4. min_4_version_apps_sub_properties is using min_4_version_apps_properties, so it would a child of B1, naming it C1.
       """
}
