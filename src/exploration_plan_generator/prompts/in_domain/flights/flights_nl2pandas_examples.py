flights_nl2pandas_examples = {
    1:
    """
task: find one flight delay reason which has one different property compared to all the other flight delay reasons

LDX:
    df = pd.read_csv("from_boston.tsv", delimiter="\t")

    some_delay_reason = df[df['delay_reason'] == <VALUE>]
    other_delay_reason = df[df['delay_reason'] != <VALUE>]

    some_delay_reason_agg = some_delay_reason.groupby(<COL>).agg(<AGG>)
    other_delay_reason_agg = other_delay_reason.groupby(<COL>).agg(<AGG>)

explanation: Split the flights to two sets - one with a certain delay reason origin airport and one the other delay reasons.
Then apply the same aggregation on both of them in order to compare them.
""",
    2:
    """
task: investigate what makes flights to have large delay and drill down to a specific reason

LDX:
    df = pd.read_csv("from_boston.tsv", delimiter="\t")
    large_delay_flights = df[df['delay_duration'] == LARGE_DELAY]
    flights_properties1 = large_delay_flights.groupby(<COL1>).agg(<AGG1>)
    focus_of_col1 = large_delay_flights[large_delay_flights[<COL1>] == <VALUE1>]
    flights_properties2 = focus_of_col1.groupby(<COL2>).agg(<AGG2>)
    focus_of_col2 = focus_of_col1[focus_of_col1[<COL2>] == <VALUE2>]

explanation: filter the flights for those with large delay.
Then, group according to some column and apply some aggregation in order to find some column that significantly influences the distribution of those flights.
After that filter on one of the values of the selected column from the previous step. Repeat it once again to drill down more.
""",
    3:
    """
task: compare some three different subsets of delay reasons of flights according to some properties

LDX:
    df = pd.read_csv("from_boston.tsv", delimiter="\t")

    first_delay_reason = df[df['delay_reason'] == <VALUE1>]
    second_delay_reason = df[df['delay_reason'] == <VALUE2>]
    third_delay_reason = df[df['delay_reason'] == <VALUE3>]

    first_delay_reason_agg = first_delay_reason.groupby(<COL>).agg(<AGG>)
    second_delay_reason_agg = second_delay_reason.groupby(<COL>).agg(<AGG>)
    third_delay_reason_agg = third_delay_reason.groupby(<COL>).agg(<AGG>)

explanation: Split the flights to three sets, each one filtered to a different delay reasons.
Then apply the same aggregation on each of them in order to compare them.
""",
    4:
    """
task: show the average departure delay of some two different subsets of flights

LDX:
    df = pd.read_csv("from_boston.tsv", delimiter="\t")

    first_subset = df[df[<COL1>] == <VALUE1>]
    first_subset_agg = first_subset.groupby(<AGG_COL1>).agg({'departure_delay': 'mean'})

    second_subset = df[df[<COL2] == <VALUE2>]
    second_subset_agg = second_subset.groupby(<AGG_COL2>).agg({'departure_delay': 'mean'})

explanation: filter the flights to some column and some of its values.
Then, group the flights according to some column and calculate the average departure delay. Do so one more time but on different subset of the flights.
""",
    5:
    """
task: show two properties of flights with departure delay compared to all the flights

LDX:
    df = pd.read_csv("from_boston.tsv", delimiter="\t")

    flights_properties_1 = df.groupby(<COL1>).agg(<AGG1>)
    flights_properties_2 = df.groupby(<COL2>).agg(<AGG2>)

    flights_with_departure_delay = df[df['departure_delay'] != 'ON_TIME']
    flights_with_departure_delay_properties1 = flights_with_departure_delay.groupby(<COL1>).agg(<AGG1>)
    flights_with_departure_delay_properties2 = flights_with_departure_delay.groupby(<COL2>).agg(<AGG2>)

explanation: Apply two aggregations. Also filter the original data to flights didn't depart on time and apply the same two aggregations in order to compare it to the previous step.
""",
    6:
    """
task: explore three different origin airports in different ways

LDX:
    df = pd.read_csv("from_boston.tsv", delimiter="\t")

    flights_origin_airport1 = df[df['origin_airport'] == <VALUE1>]
    flights_origin_airport2 = df[df['origin_airport'] == <VALUE2>]
    flights_origin_airport3 = df[df['origin_airport'] == <VALUE3>]

    flights_origin_airport1_properties = flights_origin_airport1.groupby(<COL1>).agg(<AGG1>)
    flights_origin_airport2_properties = flights_origin_airport2.groupby(<COL2>).agg(<AGG2>)
    flights_origin_airport3_properties = flights_origin_airport3.groupby(<COL3>).agg(<AGG3>)

explanation: filter to three different origin airports and for each one show some properties.
""",
    8:
    """
task: explore the data, make sure to address two interesting properties of flights with month equals 7

LDX:
    df = pd.read_csv("from_boston.tsv", delimiter="\t")

    do_some_operations()

    july_flights = df[df['month'] == 7]

    july_flights_properties_1 = july_flights.groupby(<COL1>).agg(<AGG1>)
    july_flights_properties_2 = july_flights.groupby(<COL2>).agg(<AGG2>)

explanation: do some operations and at in some point filter month to July. Then, show two different properties using two different group by operations.
""",
    9:
    """
task: show interesting sub-groups of flights to JFK

LDX:
    df = pd.read_csv("from_boston.tsv", delimiter="\t")

    jfk_flights = df[df['destination_airport'] == 'JFK']

    jfk_agg = jfk_flights.groupby(<COL1>).agg(<AGG1>)

    jfk_sub_agg = jfk_agg.groupby(<COL2>).agg(<AGG2>)

explanation: Filter to flights JFK as destination airport.
Then apply some groupby to view it as interesting groups, and apply another different groupby to view interesting sub-groups.
"""
}