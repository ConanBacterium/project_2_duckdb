┌─────────────────────────────────────┐
│┌───────────────────────────────────┐│
││    Query Profiling Information    ││
│└───────────────────────────────────┘│
└─────────────────────────────────────┘
EXPLAIN ANALYZE  SELECT     sum(LO_REVENUE),     D_YEAR,     P_BRAND FROM     lineorder,     date,     part,     supplier WHERE     LO_ORDERDATE = D_DATEKEY     AND LO_PARTKEY = P_PARTKEY     AND LO_SUPPKEY = S_SUPPKEY     AND P_BRAND BETWEEN     'MFGR#2221' AND 'MFGR#2228'     AND S_REGION = 'ASIA' GROUP BY     D_YEAR,     P_BRAND ORDER BY     D_YEAR,     P_BRAND;
┌────────────────────────────────────────────────┐
│┌──────────────────────────────────────────────┐│
││               Total Time: 7.42s              ││
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
│          ((mean: 0.00000, std: 0.00000, cv: 0.00000)s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│          ORDER_BY         │
│    ────────────────────   │
│      date.D_YEAR ASC      │
│      part.P_BRAND ASC     │
│                           │
│          56 Rows          │
│          ((mean: 0.00041, std: 0.00200, cv: 4.89792)s)          │
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
│          (mean: 56.00000, std: 0.00000, cv: 0.00000) Rows          │
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
│          ((mean: 0.00000, std: 0.00000, cv: 0.00000)s)          │
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
│          ((mean: 0.00000, std: 0.00000, cv: 0.00000)s)          │
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
│          ((mean: 0.05000, std: 0.00577, cv: 0.11547)s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│           D_YEAR          │
│          P_BRAND          │
│         LO_REVENUE        │
│                           │
│        966042 Rows        │
│          ((mean: 0.00000, std: 0.00000, cv: 0.00000)s)          │
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
│          ((mean: 0.03041, std: 0.00200, cv: 0.06574)s)          │
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
│          ((mean: 0.01000, std: 0.00000, cv: 0.00000)s)          │                                                                        │
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
│          ((mean: 0.04204, std: 0.00407, cv: 0.09686)s)          │                                           │              │          ((mean: 0.00122, std: 0.00331, cv: 2.70481)s)          │
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
│          ((mean: 2.13918, std: 0.11197, cv: 0.05234)s)          │              │              │          ((mean: 0.00469, std: 0.00680, cv: 1.44899)s)          │
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
│          ((mean: 42.48020, std: 4.43894, cv: 0.10449)s)         ││          ((mean: 0.00000, std: 0.00000, cv: 0.00000)s)          │
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
                             │          ((mean: 0.04939, std: 0.02164, cv: 0.43820)s)          │
                             └───────────────────────────┘
