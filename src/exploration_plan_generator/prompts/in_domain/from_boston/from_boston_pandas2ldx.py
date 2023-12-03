from_boston_pandas2ldx_examples = {
    1:
        """
    Pandas:
            df = pd.read_csv("from_boston.tsv", delimiter="\\t")
    
            some_delay_reason = df[df['delay_reason'] == <VALUE>]
            other_delay_reason = df[df['delay_reason'] != <VALUE>]
    
            some_delay_reason_agg = some_delay_reason.groupby(<COL>).agg(<AGG>)
            other_delay_reason_agg = other_delay_reason.groupby(<COL>).agg(<AGG>)
    
            # compare the two aggregations
            comparison = pd.concat([some_delay_reason_agg, other_delay_reason_agg], axis=1)
    LDX:
            BEGIN CHILDREN {A1,A2}
            A1 LIKE [F,delay_reason,eq,<VALUE>] and CHILDREN {B1}
              B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
            A2 LIKE [F,delay_reason,ne,<VALUE>] and CHILDREN {B2}
              B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    """,
    2:
        """
Pandas:
    df = pd.read_csv("from_boston.tsv", delimiter="\\t")
    large_delay_flights = df[df['delay_duration'] == LARGE_DELAY]
    flights_properties1 = large_delay_flights.groupby(<COL1>).agg(<AGG1>)
    focus_of_col1 = large_delay_flights[large_delay_flights[<COL1>] == <VALUE1>]
    flights_properties2 = focus_of_col1.groupby(<COL2>).agg(<AGG2>)
    focus_of_col2 = focus_of_col1[focus_of_col1[<COL2>] == <VALUE2>]
LDX:
        BEGIN CHILDREN {A1}
        A1 LIKE [F,delay_duration,eq,LARGE_DELAY] and CHILDREN {B1,B2}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        B2 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {C1,C2}
            C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
            C2 LIKE [F,<COL2>,eq,<VALUE2>]
    """,
    3:
        """
    Pandas:
        df = pd.read_csv("from_boston.tsv", delimiter="\\t")
    
        first_delay_reason = df[df['delay_reason'] == <VALUE1>]
        second_delay_reason = df[df['delay_reason'] == <VALUE2>]
        third_delay_reason = df[df['delay_reason'] == <VALUE3>]
    
        first_delay_reason_agg = first_delay_reason.groupby(<COL>).agg(<AGG>)
        second_delay_reason_agg = second_delay_reason.groupby(<COL>).agg(<AGG>)
        third_delay_reason_agg = third_delay_reason.groupby(<COL>).agg(<AGG>)
    LDX:
        BEGIN CHILDREN {A1,A2,A3}
        A1 LIKE [F,delay_reason,eq,<VALUE1>] and CHILDREN {B1}
          B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
        A2 LIKE [F,delay_reason,eq,<VALUE2>] and CHILDREN {B2}
          B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
        A3 LIKE [F,delay_reason,eq,<VALUE3>] and CHILDREN {B3}
          B3 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
        """,
    4:
        """
    Pandas:
            df = pd.read_csv("from_boston.tsv", delimiter="\\t")
    
            first_subset = df[df[<COL1>] == <VALUE1>]
            first_subset_agg = first_subset.groupby(<AGG_COL1>).agg({'departure_delay': 'mean'})
    
            second_subset = df[df[<COL2] == <VALUE2>]
            second_subset_agg = second_subset.groupby(<AGG_COL2>).agg({'departure_delay': 'mean'})
    
            highest_departure_delay = max(first_subset_agg['departure_delay'], second_subset_agg['departure_delay'])
    LDX:
            BEGIN CHILDREN {A1,A2}
            A1 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {B1}
              B1 LIKE [G,<AGG_COL1>,mean,departure_delay]
            A2 LIKE [F,<COL2>,eq,<VALUE2>] and CHILDREN {B2}
              B2 LIKE [G,<AGG_COL2>,mean,departure_delay]
        """,
    5:
        """
    Pandas:
            df = pd.read_csv("from_boston.tsv", delimiter="\\t")
    
            flights_properties_1 = df.groupby(<COL1>).agg(<AGG1>)
            flights_properties_2 = df.groupby(<COL2>).agg(<AGG2>)
    
            flights_with_departure_delay = df[df['departure_delay'] != 'ON_TIME']
            flights_with_departure_delay_properties1 = flights_with_departure_delay.groupby(<COL1>).agg(<AGG1>)
            flights_with_departure_delay_properties2 = flights_with_departure_delay.groupby(<COL2>).agg(<AGG2>)
    LDX:
            BEGIN CHILDREN {A1,A2,A3}
            A1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
            A2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
            A3 LIKE [F,departure_delay,eq,ON_TIME] and CHILDREN {B1,B2}
              B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
              B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        """,
    6:
        """
    Pandas:
        flights_origin_airport1 = df[df['origin_airport'] == <VALUE1>]
        flights_origin_airport2 = df[df['origin_airport'] == <VALUE2>]
        flights_origin_airport3 = df[df['origin_airport'] == <VALUE3>]
    
        flights_origin_airport1_properties = flights_origin_airport1.groupby(<COL1>).agg(<AGG1>)
        flights_origin_airport2_properties = flights_origin_airport2.groupby(<COL2>).agg(<AGG2>)
        flights_origin_airport3_properties = flights_origin_airport3.groupby(<COL3>).agg(<AGG3>)
    LDX:
        BEGIN CHILDREN {A1,A2,A3}
        A1 LIKE [F,origin_airport,eq,<VALUE1>] and CHILDREN {B1}
            B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        A2 LIKE [F,origin_airport,eq,<VALUE2>] and CHILDREN {B2}
            B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        A3 LIKE [F,origin_airport,eq,<VALUE3>] and CHILDREN {B3}
            B3 LIKE [G,<COL3>,<AGG_FUNC3>,<AGG_COL3>]
        """,
    8:
        """
    Pandas:
        df = pd.read_csv("from_boston.tsv", delimiter="\\t")
    
        do_some_operations()
    
        july_flights = df[df['month'] == 7]
    
        july_flights_properties_1 = july_flights.groupby(<COL1>).agg(<AGG1>)
        july_flights_properties_2 = july_flights.groupby(<COL2>).agg(<AGG2>)
    LDX:
        BEGIN DESCENDANTS {A1}
        A1 LIKE [F,month,eq,7] and CHILDREN {B1,B2}
            B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
            B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        """,
    9:
        """
   Pandas:
       df = pd.read_csv("from_boston.tsv", delimiter="\\t")
   
       jfk_flights = df[df['destination_airport'] == 'JFK']
   
       jfk_agg = jfk_flights.groupby(<COL1>).agg(<AGG1>)
   
       jfk_sub_agg = jfk_agg.groupby(<COL2>).agg(<AGG2>)
   LDX:
       BEGIN CHILDREN {A1}
       A1 LIKE [F,destination_airport,eq,JFK] and CHILDREN {B1}
           B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>] and CHILDREN {C1}
               C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
       """
}

from_boston_pandas2ldx2 = {
    1:
        """
Pandas:
        df = pd.read_csv("from_boston.tsv", delimiter="\\t")

        some_delay_reason = df[df['delay_reason'] == <VALUE>]
        other_delay_reason = df[df['delay_reason'] != <VALUE>]

        some_delay_reason_agg = some_delay_reason.groupby(<COL>).agg(<AGG>)
        other_delay_reason_agg = other_delay_reason.groupby(<COL>).agg(<AGG>)

        # compare the two aggregations
        comparison = pd.concat([some_delay_reason_agg, other_delay_reason_agg], axis=1)
LDX:
        BEGIN CHILDREN {A1,A2}
        A1 LIKE [F,delay_reason,eq,<VALUE>] and CHILDREN {B1}
          B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
        A2 LIKE [F,delay_reason,ne,<VALUE>] and CHILDREN {B2}
          B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. some_delay_reason and other_delay_reason are both using df, so they are converted to two children A1,A2 of df corresponding node which is BEGIN.
3. some_delay_reason_agg is using some_delay_reason, so it would be a node of A1, naming it B1.
4. other_delay_reason_agg is using other_delay_reason, so it would be a node of A2, naming it B2.
5. concatination isn't supported (only filter and groupby are supported), therefore the last pandas line is ignored.
    """,
    2:
        """
Pandas:
    df = pd.read_csv("from_boston.tsv", delimiter="\\t")
    large_delay_flights = df[df['delay_duration'] == LARGE_DELAY]
    flights_properties1 = large_delay_flights.groupby(<COL1>).agg(<AGG1>)
    focus_of_col1 = large_delay_flights[large_delay_flights[<COL1>] == <VALUE1>]
    flights_properties2 = focus_of_col1.groupby(<COL2>).agg(<AGG2>)
    focus_of_col2 = focus_of_col1[focus_of_col1[<COL2>] == <VALUE2>]
LDX:
        BEGIN CHILDREN {A1}
        A1 LIKE [F,delay_duration,eq,LARGE_DELAY] and CHILDREN {B1,B2}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        B2 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {C1,C2}
            C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
            C2 LIKE [F,<COL2>,eq,<VALUE2>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. large_delay_flights is using df, so it's converted to child A1 of df corresponding node, which is BEGIN.
3. flights_properties1 is using large_delay_flights, so it would be a node of A1, naming it B1.
4. focus_of_col1 is also using large_delay_flights, so it would be another node of A1, naming it B2.
5. flights_properties2 is using focus_of_col1, so it would be a node of B2, naming it C1.
6. focus_of_col2 is also using focus_of_col1, so it would be another node of B2, naming it C2.
    """,
    3:
        """
Pandas:
    df = pd.read_csv("from_boston.tsv", delimiter="\\t")

    first_delay_reason = df[df['delay_reason'] == <VALUE1>]
    second_delay_reason = df[df['delay_reason'] == <VALUE2>]
    third_delay_reason = df[df['delay_reason'] == <VALUE3>]

    first_delay_reason_agg = first_delay_reason.groupby(<COL>).agg(<AGG>)
    second_delay_reason_agg = second_delay_reason.groupby(<COL>).agg(<AGG>)
    third_delay_reason_agg = third_delay_reason.groupby(<COL>).agg(<AGG>)
LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [F,delay_reason,eq,<VALUE1>] and CHILDREN {B1}
      B1 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A2 LIKE [F,delay_reason,eq,<VALUE2>] and CHILDREN {B2}
      B2 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
    A3 LIKE [F,delay_reason,eq,<VALUE3>] and CHILDREN {B3}
      B3 LIKE [G,<COL>,<AGG_FUNC>,<AGG_COL>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. first_delay_reason, second_delay_reason and third_delay_reason are using df, so they are converted to a three children A1,A2,A3 of df corresponding node, which is BEGIN.
3. first_delay_reason_agg is using first_delay_reason, so it would be child of A1, naming it B1.
4. second_delay_reason_agg is using second_delay_reason, so it would be child of A2, naming it B2.
5. third_delay_reason_agg is using third_delay_reason, so it would be child of A3, naming it B3.
        """,
    4:
        """
Pandas:
        df = pd.read_csv("from_boston.tsv", delimiter="\\t")

        first_subset = df[df[<COL1>] == <VALUE1>]
        first_subset_agg = first_subset.groupby(<AGG_COL1>).agg({'departure_delay': 'mean'})

        second_subset = df[df[<COL2] == <VALUE2>]
        second_subset_agg = second_subset.groupby(<AGG_COL2>).agg({'departure_delay': 'mean'})

        highest_departure_delay = max(first_subset_agg['departure_delay'], second_subset_agg['departure_delay'])
LDX:
        BEGIN CHILDREN {A1,A2}
        A1 LIKE [F,<COL1>,eq,<VALUE1>] and CHILDREN {B1}
          B1 LIKE [G,<AGG_COL1>,mean,departure_delay]
        A2 LIKE [F,<COL2>,eq,<VALUE2>] and CHILDREN {B2}
          B2 LIKE [G,<AGG_COL2>,mean,departure_delay]
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
        df = pd.read_csv("from_boston.tsv", delimiter="\\t")

        flights_properties_1 = df.groupby(<COL1>).agg(<AGG1>)
        flights_properties_2 = df.groupby(<COL2>).agg(<AGG2>)

        flights_with_departure_delay = df[df['departure_delay'] != 'ON_TIME']
        flights_with_departure_delay_properties1 = flights_with_departure_delay.groupby(<COL1>).agg(<AGG1>)
        flights_with_departure_delay_properties2 = flights_with_departure_delay.groupby(<COL2>).agg(<AGG2>)
LDX:
        BEGIN CHILDREN {A1,A2,A3}
        A1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        A2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
        A3 LIKE [F,departure_delay,eq,ON_TIME] and CHILDREN {B1,B2}
          B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
          B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. flights_properties_1 and flights_properties_2 are both using df, so they are converted to two children A1,A2 of df corresponding node which is BEGIN.
3. flights_with_departure_delay is also using df, so it would be another node of BEGIN, naming it A3.
4. flights_with_departure_delay_properties1 and flights_with_departure_delay_properties2 are using flights_with_departure_delay, so they are converted to children of A3, naming them B1,B2.
        """,
    6:
        """
Pandas:
    flights_origin_airport1 = df[df['origin_airport'] == <VALUE1>]
    flights_origin_airport2 = df[df['origin_airport'] == <VALUE2>]
    flights_origin_airport3 = df[df['origin_airport'] == <VALUE3>]

    flights_origin_airport1_properties = flights_origin_airport1.groupby(<COL1>).agg(<AGG1>)
    flights_origin_airport2_properties = flights_origin_airport2.groupby(<COL2>).agg(<AGG2>)
    flights_origin_airport3_properties = flights_origin_airport3.groupby(<COL3>).agg(<AGG3>)
LDX:
    BEGIN CHILDREN {A1,A2,A3}
    A1 LIKE [F,origin_airport,eq,<VALUE1>] and CHILDREN {B1}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
    A2 LIKE [F,origin_airport,eq,<VALUE2>] and CHILDREN {B2}
        B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
    A3 LIKE [F,origin_airport,eq,<VALUE3>] and CHILDREN {B3}
        B3 LIKE [G,<COL3>,<AGG_FUNC3>,<AGG_COL3>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. flights_origin_airport1, flights_origin_airport2 and flights_origin_airport3 are using df, so they are converted to three children A1,A2,A3 of df corresponding node, which is BEGIN.
3. flights_origin_airport1_properties is using flights_origin_airport1, so it would be a child A1, naming it B1.
4. flights_origin_airport2_properties is using flights_origin_airport2, so it would be a child A2, naming it B2.
5. flights_origin_airport3_properties is using flights_origin_airport3, so it would be a child A3, naming it B3.
        """,
    8:
        """
Pandas:
    df = pd.read_csv("from_boston.tsv", delimiter="\\t")

    do_some_operations()

    july_flights = df[df['month'] == 7]

    july_flights_properties_1 = july_flights.groupby(<COL1>).agg(<AGG1>)
    july_flights_properties_2 = july_flights.groupby(<COL2>).agg(<AGG2>)
LDX:
    BEGIN DESCENDANTS {A1}
    A1 LIKE [F,month,eq,7] and CHILDREN {B1,B2}
        B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>]
        B2 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. do_some_operations() indicates that the next operation would be converted to a descendant and not a direct child, since there are some operations applied between the two.
3. july_flights is using df, so it would a be a descendant of df corresponding node, which is BEGIN.
4. july_flights_properties_1, july_flights_properties_2 are using july_flights, so they would be two children of A1, naming them B1,B2 respectively.
        """,
    9:
        """
Pandas:
   df = pd.read_csv("from_boston.tsv", delimiter="\\t")

   jfk_flights = df[df['destination_airport'] == 'JFK']

   jfk_agg = jfk_flights.groupby(<COL1>).agg(<AGG1>)

   jfk_sub_agg = jfk_agg.groupby(<COL2>).agg(<AGG2>)
LDX:
   BEGIN CHILDREN {A1}
   A1 LIKE [F,destination_airport,eq,JFK] and CHILDREN {B1}
       B1 LIKE [G,<COL1>,<AGG_FUNC1>,<AGG_COL1>] and CHILDREN {C1}
           C1 LIKE [G,<COL2>,<AGG_FUNC2>,<AGG_COL2>]
explanation:
1. loading the dataset into df is converted to the BEGIN node which doesn't do any analytic operation.
2. jfk_flights is using df, so it would a be a child of df corresponding node, which is BEGIN.
3. jfk_agg is using jfk_flights, so it would a child of A1, naming it B1.
4. jfk_sub_agg is using jfk_agg, so it would a child of B1, naming it C1.
       """
}