┌─────────────────────────────────────┐
│┌───────────────────────────────────┐│
││    Query Profiling Information    ││
│└───────────────────────────────────┘│
└─────────────────────────────────────┘
EXPLAIN ANALYZE  SELECT     sum(LO_REVENUE),     D_YEAR,     P_BRAND FROM     lineorder,     date,     part,     supplier WHERE     LO_ORDERDATE = D_DATEKEY     AND LO_PARTKEY = P_PARTKEY     AND LO_SUPPKEY = S_SUPPKEY     AND P_CATEGORY = 'MFGR#12'     AND S_REGION = 'AMERICA' GROUP BY     D_YEAR,     P_BRAND ORDER BY     D_YEAR,     P_BRAND;
┌────────────────────────────────────────────────┐
│┌──────────────────────────────────────────────┐│
││              Total Time: x̄:0.146,cv:0.053s              ││
│└──────────────────────────────────────────────┘│
└────────────────────────────────────────────────┘
┌────────────────────────────────────────────────┐
│               Optimizer: 0.0000s               │
│┌──────────────────────────────────────────────┐│
││        Build Side Probe Side: 0.0000s        ││
││           Column Lifetime: 0.0000s           ││
││           Common Aggregate: 0.0000s          ││
││        Common Subexpressions: 0.0000s        ││
││      Compressed Materialization: 0.0000s     ││
││          Cte Filter Pusher: 0.0000s          ││
││             Deliminator: 0.0000s             ││
││           Duplicate Groups: 0.0000s          ││
││         Expression Rewriter: 0.0000s         ││
││              Extension: 0.0000s              ││
││            Filter Pullup: 0.0000s            ││
││           Filter Pushdown: 0.0000s           ││
││              In Clause: 0.0000s              ││
││         Join Filter Pushdown: 0.0000s        ││
││              Join Order: 0.0000s             ││
││            Limit Pushdown: 0.0000s           ││
││           Materialized Cte: 0.0000s          ││
││             Regex Range: 0.0000s             ││
││            Reorder Filter: 0.0000s           ││
││        Statistics Propagation: 0.0000s       ││
││                Top N: 0.0000s                ││
││           Unnest Rewriter: 0.0000s           ││
││            Unused Columns: 0.0000s           ││
│└──────────────────────────────────────────────┘│
└────────────────────────────────────────────────┘
┌────────────────────────────────────────────────┐
│            Physical planner: 0.0000s           │
│┌──────────────────────────────────────────────┐│
││            Column Binding: 0.0000s           ││
││             Create Plan: 0.0000s             ││
││            Resolve Types: 0.0000s            ││
│└──────────────────────────────────────────────┘│
└────────────────────────────────────────────────┘
┌────────────────────────────────────────────────┐
│                Planner: 0.0000s                │
│┌──────────────────────────────────────────────┐│
││               Binding: 0.0000s               ││
│└──────────────────────────────────────────────┘│
└────────────────────────────────────────────────┘
┌───────────────────────────┐
│           QUERY           │
│    ────────────────────   │
│           0 Rows          │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│      EXPLAIN_ANALYZE      │
│    ────────────────────   │
│           0 Rows          │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│             #0            │
│__internal_decompress_integ│
│   ral_smallint(#1, 1992)  │
│__internal_decompress_strin│
│           g(#2)           │
│                           │
│          280 Rows         │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│          ORDER_BY         │
│    ────────────────────   │
│      date.D_YEAR ASC      │
│      part.P_BRAND ASC     │
│                           │
│          280 Rows         │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│             #0            │
│__internal_compress_integra│
│    l_utinyint(#1, 1992)   │
│__internal_compress_string_│
│        hugeint(#2)        │
│                           │
│          280 Rows         │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│      sum(LO_REVENUE)      │
│           D_YEAR          │
│          P_BRAND          │
│                           │
│          280 Rows         │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│__internal_decompress_integ│
│   ral_smallint(#0, 1992)  │
│__internal_decompress_strin│
│           g(#1)           │
│             #2            │
│                           │
│          280 Rows         │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│       HASH_GROUP_BY       │
│    ────────────────────   │
│          Groups:          │
│             #0            │
│             #1            │
│                           │
│    Aggregates: sum(#2)    │
│                           │
│          280 Rows         │
│          (x̄:0.013,cv:0.357s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│           D_YEAR          │
│          P_BRAND          │
│         LO_REVENUE        │
│                           │
│        490522 Rows        │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│             #0            │
│             #1            │
│__internal_compress_integra│
│     l_usmallint(#2, 1)    │
│             #3            │
│             #4            │
│__internal_compress_string_│
│        hugeint(#5)        │
│__internal_compress_integra│
│     l_usmallint(#6, 1)    │
│             #7            │
│__internal_compress_integra│
│    l_utinyint(#8, 1992)   │
│                           │
│        490522 Rows        │
│          (x̄:0.010,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         HASH_JOIN         │
│    ────────────────────   │
│      Join Type: INNER     │
│                           │
│        Conditions:        │
│  LO_ORDERDATE = D_DATEKEY │
│                           ├────────────────────────────────────────────────────────────────────────┐
│   Build Min: 1992-01-02   │                                                                        │
│   Build Max: 1998-12-30   │                                                                        │
│                           │                                                                        │
│        490522 Rows        │                                                                        │
│          (x̄:0.000,cv:0.000s)          │                                                                        │
└─────────────┬─────────────┘                                                                        │
┌─────────────┴─────────────┐                                                          ┌─────────────┴─────────────┐
│         HASH_JOIN         │                                                          │         TABLE_SCAN        │
│    ────────────────────   │                                                          │    ────────────────────   │
│      Join Type: INNER     │                                                          │            date           │
│                           │                                                          │                           │
│        Conditions:        │                                                          │        Projections:       │
│   LO_SUPPKEY = S_SUPPKEY  │                                                          │         D_DATEKEY         │
│                           ├───────────────────────────────────────────┐              │           D_YEAR          │
│        Build Min: 1       │                                           │              │                           │
│      Build Max: 20000     │                                           │              │                           │
│                           │                                           │              │                           │
│        490522 Rows        │                                           │              │         2555 Rows         │
│          (x̄:0.130,cv:0.064s)          │                                           │              │          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘                                           │              └───────────────────────────┘
┌─────────────┴─────────────┐                             ┌─────────────┴─────────────┐
│         HASH_JOIN         │                             │         TABLE_SCAN        │
│    ────────────────────   │                             │    ────────────────────   │
│      Join Type: INNER     │                             │          supplier         │
│                           │                             │                           │
│        Conditions:        │                             │        Projections:       │
│   LO_PARTKEY = P_PARTKEY  │                             │         S_SUPPKEY         │
│                           ├──────────────┐              │                           │
│        Build Min: 1       │              │              │          Filters:         │
│     Build Max: 600000     │              │              │   S_REGION='AMERICA' AND  │
│                           │              │              │    S_REGION IS NOT NULL   │
│                           │              │              │                           │
│        2392757 Rows       │              │              │         4102 Rows         │
│          (x̄:0.180,cv:0.058s)          │              │              │          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘              │              └───────────────────────────┘
┌─────────────┴─────────────┐┌─────────────┴─────────────┐
│         TABLE_SCAN        ││           FILTER          │
│    ────────────────────   ││    ────────────────────   │
│         lineorder         ││   (P_PARTKEY <= 600000)   │
│                           ││                           │
│        Projections:       ││                           │
│        LO_ORDERDATE       ││                           │
│         LO_PARTKEY        ││                           │
│         LO_SUPPKEY        ││                           │
│         LO_REVENUE        ││                           │
│                           ││                           │
│       59943219 Rows       ││         23943 Rows        │
│          (x̄:0.733,cv:0.054s)          ││          (x̄:0.000,cv:0.000s)          │
└───────────────────────────┘└─────────────┬─────────────┘
                             ┌─────────────┴─────────────┐
                             │         TABLE_SCAN        │
                             │    ────────────────────   │
                             │            part           │
                             │                           │
                             │        Projections:       │
                             │         P_PARTKEY         │
                             │          P_BRAND          │
                             │                           │
                             │          Filters:         │
                             │  P_CATEGORY='MFGR#12' AND │
                             │   P_CATEGORY IS NOT NULL  │
                             │                           │
                             │         31882 Rows        │
                             │          (x̄:0.001,cv:3.956s)          │
                             └───────────────────────────┘
