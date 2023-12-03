from_boston_nl2ldx_examples = {
    1:
    """
task: find one flight delay reason which has one different property compared to all the other flight delay reasons

LDX:
    BEGIN CHILDREN {A1,A2}
    A1 LIKE [F,delay_reason,eq,<VALUE>] and CHILDREN {B1}
      B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A2 LIKE [F,delay_reason,ne,<VALUE>] and CHILDREN {B2}
      B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]

explanation: Split the flights to two sets - one with a certain delay reason origin airport and one with the other delay reasons.
Then apply the same aggregation on both of them in order to compare them.
""",
    2:
    """
task: investigate what makes flights to have large delay and drill down to a specific reason

LDX:
    BEGIN CHILDREN {A1}
    A1 LIKE [F,delay_duration,eq,LARGE_DELAY] and CHILDREN {B1,B2}
    B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    B2 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {C1,C2}
        C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        C2 LIKE [F,<COL2>,eq,<VALUE2>]

explanation: filter the flights for those with large delay.
Then, group according to some column and apply some aggregation in order to find some column that significantly influences the distribution of those flights.
After that filter on one of the values of the selected column from the previous step. Repeat it once again to drill down more.
""",
    3:
    """
task: compare some three different subsets of delay reasons according to some properties

LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [F,delay_reason,eq,<VALUE1>] and CHILDREN {B1}
      B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A2 LIKE [F,delay_reason,eq,<VALUE2>] and CHILDREN {B2}
      B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A3 LIKE [F,delay_reason,eq,<VALUE3>] and CHILDREN {B3}
      B3 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]

explanation: Split the flights to three sets, each one filtered to a different delay reason.
Then apply the same aggregation on each of them in order to compare them.
""",
    4:
    """
task: show the average departure delay of some two different subsets of flights

LDX:
    BEGIN CHILDREN {A1,A2}
    A1 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {B1}
      B1 LIKE [G,<AGG_COL1>,mean,departure_delay]
    A2 LIKE [F,<COL2>,eq,<VALUE2>] and CHILDREN {B2}
      B2 LIKE [G,<AGG_COL2>,mean,departure_delay]

explanation: filter the flights to some column and some of its values.
Then, group the flights according to some column and calculate the average departure delay. Do so one more time but on different subset of the flights.
""",
    5:
    """
task: show two properties of flights with departure delay compared to all the flights

LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    A2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    A3 LIKE [F,departure_delay,ne,ON_TIME] and CHILDREN {B1,B2}
      B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
      B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]

explanation: Apply two aggregations. Also filter the original data to flights didn't depart on time and apply the same two aggregations in order to compare it to the previous step.
""",
    6:
    """
task: explore three different origin airports in different ways

LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [F,origin_airport,eq,<VALUE1>] and CHILDREN {B1}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    A2 LIKE [F,origin_airport,eq,<VALUE2>] and CHILDREN {B2}
        B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    A3 LIKE [F,origin_airport,eq,<VALUE3>] and CHILDREN {B3}
        B3 LIKE [G,<COL3>,<AGG_FUNC3>,<AGG_COL3>]

explanation: filter to three different origin airports and for each one show some properties.
   """,
    8:
    """
task: explore the data, make sure to address two interesting aspects of flights with month equals 7

LDX:
    BEGIN DESCENDANTS {A1}
    A1 LIKE [F,month,eq,7] and CHILDREN {B1,B2}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]

explanation: Use descendant in order to filter month to July at some point. Then, show two different properties using two different group by operations.
""",
    9:
    """
task: show interesting sub-groups of flights to JFK
LDX:
    BEGIN CHILDREN {A1}
    A1 LIKE [F,destination_airport,eq,JFK] and CHILDREN {B1}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>] and CHILDREN {C1}
            C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
explanation: Filter to flights JFK as destination airport.
Then apply some groupby to view it as interesting groups, and apply another different groupby to view interesting sub-groups.
"""
}