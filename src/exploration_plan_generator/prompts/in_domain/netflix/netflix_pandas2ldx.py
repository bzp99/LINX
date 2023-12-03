netflix_pandas2ldx_examples = {
    1:
    """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    some_rating = df[df['rating'] == <VALUE>]
    other_rating = df[df['rating'] != <VALUE>]

    some_rating_agg = some_rating.groupby(<COL>).agg(<AGG>)
    other_rating_agg = other_rating.groupby(<COL>).agg(<AGG>)
    
    # compare the two aggregations
    comparison = pd.concat([some_rating_agg, other_rating_agg], axis=1)
LDX:
    BEGIN CHILDREN {A1,A2}
    A1 LIKE [F,rating,eq,<VALUE>] and CHILDREN {B1}
      B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A2 LIKE [F,rating,ne,<VALUE>] and CHILDREN {B2}
      B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
""",
    2:
        """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    christopher_nolan_shows = df[df['director'] == 'Christopher Nolan']

    shows_properties1 = christopher_nolan_shows.groupby(<COL1>).agg(<AGG1>)

    focus_of_col1 = christopher_nolan_shows[christopher_nolan_shows[<COL1>] == <VALUE1>]

    shows_properties2 = focus_of_col1.groupby(<COL2>).agg(<AGG2>)

    focus_of_col2 = focus_of_col1[focus_of_col1[<COL2>] == <VALUE2>]
LDX:
    BEGIN CHILDREN {A1}
    A1 LIKE [F,director,eq,Christopher Nolan] and CHILDREN {B1,B2}
    B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    B2 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {C1,C2}
        C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        C2 LIKE [F,<COL2>,eq,<VALUE2>]
    """,
    3:
    """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    first_director = df[df['director'] == <VALUE1>]
    second_director = df[df['director'] == <VALUE2>]
    third_director = df[df['director'] == <VALUE3>]

    first_director_agg = first_director.groupby(<COL>).agg(<AGG>)
    second_director_agg = second_director.groupby(<COL>).agg(<AGG>)
    third_director_agg = third_director.groupby(<COL>).agg(<AGG>)
LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [F,director,eq,<VALUE1>] and CHILDREN {B1}
      B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A2 LIKE [F,director,eq,<VALUE2>] and CHILDREN {B2}
      B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A3 LIKE [F,director,eq,<VALUE3>] and CHILDREN {B3}
      B3 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    """,
    4:
    """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    first_subset = df[df[<COL1>] == <VALUE1>]
    first_subset_agg = first_subset.groupby(<AGG_COL1>).agg({'duration': 'mean'})

    second_subset = df[df[<COL2] == <VALUE2>]
    second_subset_agg = second_subset.groupby(<AGG_COL2>).agg({'duration': 'mean'})
    
    highest_duration = max(first_subset_agg['duration'], second_subset_agg['duration'])
LDX:
    BEGIN CHILDREN {A1,A2}
    A1 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {B1}
      B1 LIKE [G,<AGG_COL1>,mean,duration]
    A2 LIKE [F,<COL2>,eq,<VALUE2>] and CHILDREN {B2}
      B2 LIKE [G,<AGG_COL2>,mean,duration]
    """,
    5:
    """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    shows_properties_1 = df.groupby(<COL1>).agg(<AGG1>)
    shows_properties_2 = df.groupby(<COL2>).agg(<AGG2>)

    hero_shows = df['Hero' in df['title']]
    hero_shows_properties_1 = hero_shows.groupby(<COL1>).agg(<AGG1>)
    hero_shows_properties_2 = hero_shows.groupby(<COL2>).agg(<AGG2>)
LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    A2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    A3 LIKE [F,title,contains,Hero] and CHILDREN {B1,B2}
      B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
      B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    """,
    6:
    """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    release_year1_shows = df[df['release_year'] == <VALUE1>]
    release_year2_shows = df[df['release_year'] == <VALUE2>]
    release_year3_shows = df[df['release_year'] == <VALUE3>]

    release_year1_shows_properties = release_year1_shows.groupby(<COL1>).agg(<AGG1>)
    release_year2_shows_properties = release_year2_shows.groupby(<COL2>).agg(<AGG2>)
    release_year3_shows_properties = release_year3_shows.groupby(<COL3>).agg(<AGG3>)
LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [F,release_year,eq,<VALUE1>] and CHILDREN {B1}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    A2 LIKE [F,release_year,eq,<VALUE2>] and CHILDREN {B2}
        B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    A3 LIKE [F,release_year,eq,<VALUE3>] and CHILDREN {B3}
        B3 LIKE [G,<COL3>,<AGG_FUNC3>,<AGG_COL3>]
    """,
    8:
    """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    do_some_operations()

    tv_14_shows = df[df['rating'] == 'TV-14']

    tv_14_shows_properties1 = tv_14_shows.groupby(<COL1>).agg(<AGG1>)
    tv_14_shows_properties2 = tv_14_shows.groupby(<COL2>).agg(<AGG2>)
LDX:
    BEGIN DESCENDANTS {A1}
    A1 LIKE [F,rating,eq,TV-14] and CHILDREN {B1,B2}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    """,
    9:
     """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    israel_shows = df[df['country'] == 'Israel']

    israel_shows_properties = israel_shows.groupby(<COL1>).agg(<AGG1>)
    israel_shows_sub_properties = israel_shows_properties.groupby(<COL2>).agg(<AGG2>)
LDX:
    BEGIN CHILDREN {A1}
    A1 LIKE [F,country,eq,Israel] and CHILDREN {B1}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>] and CHILDREN {C1}
            C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    """
}

netflix_pandas2ldx2 = {
    1:
        """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    some_rating = df[df['rating'] == <VALUE>]
    other_rating = df[df['rating'] != <VALUE>]

    some_rating_agg = some_rating.groupby(<COL>).agg(<AGG>)
    other_rating_agg = other_rating.groupby(<COL>).agg(<AGG>)

    # compare the two aggregations
    comparison = pd.concat([some_rating_agg, other_rating_agg], axis=1)
LDX:
    BEGIN CHILDREN {A1,A2}
    A1 LIKE [F,rating,eq,<VALUE>] and CHILDREN {B1}
      B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A2 LIKE [F,rating,ne,<VALUE>] and CHILDREN {B2}
      B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. some_rating and other_rating are both using df, so they are converted to two children A1,A2 of df corresponding node which is BEGIN.
3. some_rating_agg is using some_rating, so it would be a node of A1, naming it B1.
4. other_rating_agg is using other_rating, so it would be a node of A2, naming it B2.
5. concatination isn't supported (only filter and groupby are supported), therefore the last pandas line is ignored.
    """,
    2:
        """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    christopher_nolan_shows = df[df['director'] == 'Christopher Nolan']

    shows_properties1 = christopher_nolan_shows.groupby(<COL1>).agg(<AGG1>)

    focus_of_col1 = christopher_nolan_shows[christopher_nolan_shows[<COL1>] == <VALUE1>]

    shows_properties2 = focus_of_col1.groupby(<COL2>).agg(<AGG2>)

    focus_of_col2 = focus_of_col1[focus_of_col1[<COL2>] == <VALUE2>]
LDX:
    BEGIN CHILDREN {A1}
    A1 LIKE [F,director,eq,Christopher Nolan] and CHILDREN {B1,B2}
    B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    B2 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {C1,C2}
        C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        C2 LIKE [F,<COL2>,eq,<VALUE2>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. christopher_nolan_shows is using df, so it's converted to child A1 of df corresponding node, which is BEGIN.
3. shows_properties1 is using christopher_nolan_shows, so it would be a node of A1, naming it B1.
4. focus_of_col1 is also using christopher_nolan_shows, so it would be another node of A1, naming it B2.
5. shows_properties2 is using focus_of_col1, so it would be a node of B2, naming it C1.
6. focus_of_col2 is also using focus_of_col1, so it would be another node of B2, naming it C2.
    """,
    3:
        """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    first_director = df[df['director'] == <VALUE1>]
    second_director = df[df['director'] == <VALUE2>]
    third_director = df[df['director'] == <VALUE3>]

    first_director_agg = first_director.groupby(<COL>).agg(<AGG>)
    second_director_agg = second_director.groupby(<COL>).agg(<AGG>)
    third_director_agg = third_director.groupby(<COL>).agg(<AGG>)
LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [F,director,eq,<VALUE1>] and CHILDREN {B1}
      B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A2 LIKE [F,director,eq,<VALUE2>] and CHILDREN {B2}
      B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A3 LIKE [F,director,eq,<VALUE3>] and CHILDREN {B3}
      B3 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. first_director, second_director and third_director are using df, so they are converted to a three children A1,A2,A3 of df corresponding node, which is BEGIN.
3. first_director_agg is using first_director, so it would be child of A1, naming it B1.
4. second_director_agg is using second_director, so it would be child of A2, naming it B2.
5. third_director_agg is using third_director, so it would be child of A3, naming it B3.
        """,
    4:
    """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    first_subset = df[df[<COL1>] == <VALUE1>]
    first_subset_agg = first_subset.groupby(<AGG_COL1>).agg({'duration': 'mean'})

    second_subset = df[df[<COL2] == <VALUE2>]
    second_subset_agg = second_subset.groupby(<AGG_COL2>).agg({'duration': 'mean'})

    highest_duration = max(first_subset_agg['duration'], second_subset_agg['duration'])
LDX:
    BEGIN CHILDREN {A1,A2}
    A1 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {B1}
      B1 LIKE [G,<AGG_COL1>,mean,duration]
    A2 LIKE [F,<COL2>,eq,<VALUE2>] and CHILDREN {B2}
      B2 LIKE [G,<AGG_COL2>,mean,duration]
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
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    shows_properties_1 = df.groupby(<COL1>).agg(<AGG1>)
    shows_properties_2 = df.groupby(<COL2>).agg(<AGG2>)

    hero_shows = df['Hero' in df['title']]
    hero_shows_properties_1 = hero_shows.groupby(<COL1>).agg(<AGG1>)
    hero_shows_properties_2 = hero_shows.groupby(<COL2>).agg(<AGG2>)
LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    A2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    A3 LIKE [F,title,contains,Hero] and CHILDREN {B1,B2}
      B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
      B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. shows_properties_1 and shows_properties_2 are both using df, so they are converted to two children A1,A2 of df corresponding node which is BEGIN.
3. hero_shows is also using df, so it would be another node of BEGIN, naming it A3.
4. hero_shows_properties_1 and hero_shows_properties_2 are using hero_shows, so they are converted to children of A3, naming them B1,B2.
        """,
    6:
        """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    release_year1_shows = df[df['release_year'] == <VALUE1>]
    release_year2_shows = df[df['release_year'] == <VALUE2>]
    release_year3_shows = df[df['release_year'] == <VALUE3>]

    release_year1_shows_properties = release_year1_shows.groupby(<COL1>).agg(<AGG1>)
    release_year2_shows_properties = release_year2_shows.groupby(<COL2>).agg(<AGG2>)
    release_year3_shows_properties = release_year3_shows.groupby(<COL3>).agg(<AGG3>)
LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [F,release_year,eq,<VALUE1>] and CHILDREN {B1}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    A2 LIKE [F,release_year,eq,<VALUE2>] and CHILDREN {B2}
        B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    A3 LIKE [F,release_year,eq,<VALUE3>] and CHILDREN {B3}
        B3 LIKE [G,<COL3>,<AGG_FUNC3>,<AGG_COL3>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. release_year1_shows, release_year2_shows and release_year3_shows are using df, so they are converted to three children A1,A2,A3 of df corresponding node, which is BEGIN.
3. release_year1_shows_properties is using release_year1_shows, so it would be a child A1, naming it B1.
4. release_year2_shows_properties is using release_year2_shows, so it would be a child A2, naming it B2.
5. release_year3_shows_properties is using release_year3_shows, so it would be a child A3, naming it B3.
        """,
    8:
        """
Pandas:
    df = pd.read_csv("netflix.tsv", delimiter="\\t")

    do_some_operations()

    tv_14_shows = df[df['rating'] == 'TV-14']

    tv_14_shows_properties1 = tv_14_shows.groupby(<COL1>).agg(<AGG1>)
    tv_14_shows_properties2 = tv_14_shows.groupby(<COL2>).agg(<AGG2>)
LDX:
    BEGIN DESCENDANTS {A1}
    A1 LIKE [F,rating,eq,TV-14] and CHILDREN {B1,B2}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. do_some_operations() indicates that the next operation would be converted to a descendant and not a direct child, since there are some operations applied between the two.
3. tv_14_shows is using df, so it would a be a descendant of df corresponding node, which is BEGIN.
4. tv_14_shows_properties1, tv_14_shows_properties2 are using tv_14_shows, so they would be two children of A1, naming them B1,B2 respectively.
        """,
    9:
        """
Pandas:
   df = pd.read_csv("netflix.tsv", delimiter="\\t")

   israel_shows = df[df['country'] == 'Israel']

   israel_shows_properties = israel_shows.groupby(<COL1>).agg(<AGG1>)
   israel_shows_sub_properties = israel_shows_properties.groupby(<COL2>).agg(<AGG2>)
LDX:
   BEGIN CHILDREN {A1}
   A1 LIKE [F,country,eq,Israel] and CHILDREN {B1}
       B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>] and CHILDREN {C1}
           C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. israel_shows is using df, so it would a be a child of df corresponding node, which is BEGIN.
3. israel_shows_properties is using israel_shows, so it would a child of A1, naming it B1.
4. israel_shows_sub_properties is using israel_shows_properties, so it would a child of B1, naming it C1.
       """
}