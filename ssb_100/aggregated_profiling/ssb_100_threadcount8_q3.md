┌─────────────────────────────────────┐
│┌───────────────────────────────────┐│
││    Query Profiling Information    ││
│└───────────────────────────────────┘│
└─────────────────────────────────────┘
EXPLAIN ANALYZE  SELECT     sum(LO_REVENUE),     D_YEAR,     P_BRAND FROM     lineorder,     date,     part,     supplier WHERE     LO_ORDERDATE = D_DATEKEY     AND LO_PARTKEY = P_PARTKEY     AND LO_SUPPKEY = S_SUPPKEY     AND P_BRAND BETWEEN     'MFGR#2221' AND 'MFGR#2228'     AND S_REGION = 'ASIA' GROUP BY     D_YEAR,     P_BRAND ORDER BY     D_YEAR,     P_BRAND;
┌────────────────────────────────────────────────┐
│┌──────────────────────────────────────────────┐│
││               Total Time: x̄:5.647,cv:0.100s              ││
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
│          56 Rows          │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│          ORDER_BY         │
│    ────────────────────   │
│      date.D_YEAR ASC      │
│      part.P_BRAND ASC     │
│                           │
│          56 Rows          │
│          (x̄:0.000,cv:4.898s)          │
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
│          x̄:56.000,cv:0.000 Rows          │
│          (0.00s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│      sum(LO_REVENUE)      │
│           D_YEAR          │
│          P_BRAND          │
│                           │
│          56 Rows          │
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
│          56 Rows          │
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
│          56 Rows          │
│          (x̄:0.050,cv:0.115s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│           D_YEAR          │
│          P_BRAND          │
│         LO_REVENUE        │
│                           │
│        966042 Rows        │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│             #0            │
│             #1            │
│             #2            │
│             #3            │
│             #4            │
│__internal_compress_string_│
│        hugeint(#5)        │
│             #6            │
│             #7            │
│__internal_compress_integra│
│    l_utinyint(#8, 1992)   │
│                           │
│        966042 Rows        │
│          (x̄:0.030,cv:0.066s)          │
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
│        966042 Rows        │                                                                        │
│          (x̄:0.010,cv:0.000s)          │                                                                        │
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
│     Build Max: 200000     │                                           │              │                           │
│                           │                                           │              │                           │
│        966042 Rows        │                                           │              │         2555 Rows         │
│          (x̄:0.042,cv:0.097s)          │                                           │              │          (x̄:0.001,cv:2.705s)          │
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
│     Build Max: 1000000    │              │              │    S_REGION='ASIA' AND    │
│                           │              │              │    S_REGION IS NOT NULL   │
│                           │              │              │                           │
│        4810374 Rows       │              │              │         40119 Rows        │
│          (x̄:2.139,cv:0.052s)          │              │              │          (x̄:0.005,cv:1.449s)          │
└─────────────┬─────────────┘              │              └───────────────────────────┘
┌─────────────┴─────────────┐┌─────────────┴─────────────┐
│         TABLE_SCAN        ││           FILTER          │
│    ────────────────────   ││    ────────────────────   │
│         lineorder         ││   (P_PARTKEY <= 1000000)  │
│                           ││                           │
│        Projections:       ││                           │
│        LO_ORDERDATE       ││                           │
│         LO_PARTKEY        ││                           │
│         LO_SUPPKEY        ││                           │
│         LO_REVENUE        ││                           │
│                           ││                           │
│       599620422 Rows      ││         8015 Rows         │
│          (x̄:42.480,cv:0.104s)         ││          (x̄:0.000,cv:0.000s)          │
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
                             │  P_BRAND>='MFGR#2221' AND │
                             │  P_BRAND<='MFGR#2228' AND │
                             │     P_BRAND IS NOT NULL   │
                             │                           │
                             │         11270 Rows        │
                             │          (x̄:0.049,cv:0.438s)          │
                             └───────────────────────────┘
