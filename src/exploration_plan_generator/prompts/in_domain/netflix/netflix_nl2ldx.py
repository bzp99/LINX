netflix_nl2ldx_examples = {
    1:
    """
task: find one rating which has one different property compared to all the other ratings

LDX:
    BEGIN CHILDREN {A1,A2}
    A1 LIKE [F,rating,eq,<VALUE>] and CHILDREN {B1}
      B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A2 LIKE [F,rating,ne,<VALUE>] and CHILDREN {B2}
      B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]

explanation: Split the shows to two sets - one with a certain rating and one with the other ratings.
Then apply the same aggregation on both of them in order to compare them.
""",
    2:
    """
task: investigate what makes shows to be directed by Christopher Nolan and drill down to a specific reason

LDX:
    BEGIN CHILDREN {A1}
    A1 LIKE [F,director,eq,Christopher Nolan] and CHILDREN {B1,B2}
    B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    B2 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {C1,C2}
        C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        C2 LIKE [F,<COL2>,eq,<VALUE2>]

explanation: filter the shows to those directed by Christopher Nolan.
Then, group according to some column and apply some aggregation in order to find some column that significantly influences the distribution of those shows.
After that filter on one of the values of the selected column from the previous step. Repeat it once again to drill down more.
""",
    3:
    """
task: compare some three different subsets of directors according to some properties

LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [F,director,eq,<VALUE1>] and CHILDREN {B1}
      B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A2 LIKE [F,director,eq,<VALUE2>] and CHILDREN {B2}
      B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A3 LIKE [F,director,eq,<VALUE3>] and CHILDREN {B3}
      B3 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]

explanation: Split the shows to three sets, each one filtered to a different director.
Then apply the same aggregation on each of them in order to compare them.
""",
    4:
    """
task: show the average duration of some two different subsets of shows

LDX:
    BEGIN CHILDREN {A1,A2}
    A1 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {B1}
      B1 LIKE [G,<AGG_COL1>,mean,duration]
    A2 LIKE [F,<COL2>,eq,<VALUE2>] and CHILDREN {B2}
      B2 LIKE [G,<AGG_COL2>,mean,duration]

explanation: filter the shows to some column and some of its values.
Then, group the shows according to some column and calculate the average duration. Do so one more time but on different subset of the shows.
""",
    5:
    """
task: show two properties of the show "Hero" compared to all the shows

LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    A2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    A3 LIKE [F,title,contains,Hero] and CHILDREN {B1,B2}
      B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
      B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]

explanation: Apply two aggregations. Also filter to show with title contains "Hero" show and apply the same two aggregations in order to compare it to the previous step.
""",
    6:
    """
task: explore three different release years in different ways

LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [F,release_year,eq,<VALUE1>] and CHILDREN {B1}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    A2 LIKE [F,release_year,eq,<VALUE2>] and CHILDREN {B2}
        B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    A3 LIKE [F,release_year,eq,<VALUE3>] and CHILDREN {B3}
        B3 LIKE [G,<COL3>,<AGG_FUNC3>,<AGG_COL3>]

explanation: filter to three different release years and for each one show some properties.
   """,
    8:
    """
task: explore the data, make sure to address two interesting aspects of shows with rating TV-14

LDX:
    BEGIN DESCENDANTS {A1}
    A1 LIKE [F,rating,eq,TV-14] and CHILDREN {B1,B2}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]

explanation: Use descendant in order to filter rating to TV-14 at some point. Then, show two different properties using two different group by operations.
""",
    9:
    """
task: show interesting sub-groups of shows filmed in Israel

LDX:
    BEGIN CHILDREN {A1}
    A1 LIKE [F,country,eq,Israel] and CHILDREN {B1}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>] and CHILDREN {C1}
            C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]

explanation: Filter to shows filmed in Israel.
Then apply some groupby to view it as interesting groups, and apply another different groupby to view interesting sub-groups.
"""
}