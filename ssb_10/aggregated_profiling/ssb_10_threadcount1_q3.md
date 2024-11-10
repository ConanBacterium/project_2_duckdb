┌─────────────────────────────────────┐
│┌───────────────────────────────────┐│
││    Query Profiling Information    ││
│└───────────────────────────────────┘│
└─────────────────────────────────────┘
EXPLAIN ANALYZE  SELECT     sum(LO_REVENUE),     D_YEAR,     P_BRAND FROM     lineorder,     date,     part,     supplier WHERE     LO_ORDERDATE = D_DATEKEY     AND LO_PARTKEY = P_PARTKEY     AND LO_SUPPKEY = S_SUPPKEY     AND P_BRAND BETWEEN     'MFGR#2221' AND 'MFGR#2228'     AND S_REGION = 'ASIA' GROUP BY     D_YEAR,     P_BRAND ORDER BY     D_YEAR,     P_BRAND;
┌────────────────────────────────────────────────┐
│┌──────────────────────────────────────────────┐│
││              Total Time: x̄:0.717,cv:0.074s              ││
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
│          56 Rows          │
│          (x̄:0.000,cv:0.000s)          │
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
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│           D_YEAR          │
│          P_BRAND          │
│         LO_REVENUE        │
│                           │
│         94802 Rows        │
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
│__internal_compress_integra│
│     l_usmallint(#4, 1)    │
│             #5            │
│__internal_compress_string_│
│        hugeint(#6)        │
│             #7            │
│__internal_compress_integra│
│    l_utinyint(#8, 1992)   │
│                           │
│         94802 Rows        │
│          (x̄:0.000,cv:0.000s)          │
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
│         94802 Rows        │                                                                        │
│          (x̄:0.000,cv:0.000s)          │                                                                        │
└─────────────┬─────────────┘                                                                        │
┌─────────────┴─────────────┐                                                          ┌─────────────┴─────────────┐
│         HASH_JOIN         │                                                          │         TABLE_SCAN        │
│    ────────────────────   │                                                          │    ────────────────────   │
│      Join Type: INNER     │                                                          │            date           │
│                           │                                                          │                           │
│        Conditions:        │                                                          │        Projections:       │
│   LO_PARTKEY = P_PARTKEY  │                                                          │         D_DATEKEY         │
│                           ├───────────────────────────────────────────┐              │           D_YEAR          │
│        Build Min: 1       │                                           │              │                           │
│     Build Max: 600000     │                                           │              │                           │
│                           │                                           │              │                           │
│         94802 Rows        │                                           │              │         2555 Rows         │
│          (x̄:0.082,cv:0.106s)          │                                           │              │          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘                                           │              └───────────────────────────┘
┌─────────────┴─────────────┐                             ┌─────────────┴─────────────┐
│         HASH_JOIN         │                             │           FILTER          │
│    ────────────────────   │                             │    ────────────────────   │
│      Join Type: INNER     │                             │   (P_PARTKEY <= 600000)   │
│                           │                             │                           │
│        Conditions:        │                             │                           │
│   LO_SUPPKEY = S_SUPPKEY  │                             │                           │
│                           ├──────────────┐              │                           │
│        Build Min: 1       │              │              │                           │
│      Build Max: 20000     │              │              │                           │
│                           │              │              │                           │
│       11996332 Rows       │              │              │         4772 Rows         │
│          (x̄:0.175,cv:0.078s)          │              │              │          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘              │              └─────────────┬─────────────┘
┌─────────────┴─────────────┐┌─────────────┴─────────────┐┌─────────────┴─────────────┐
│         TABLE_SCAN        ││         TABLE_SCAN        ││         TABLE_SCAN        │
│    ────────────────────   ││    ────────────────────   ││    ────────────────────   │
│         lineorder         ││          supplier         ││            part           │
│                           ││                           ││                           │
│        Projections:       ││        Projections:       ││        Projections:       │
│        LO_ORDERDATE       ││         S_SUPPKEY         ││         P_PARTKEY         │
│         LO_PARTKEY        ││                           ││          P_BRAND          │
│         LO_SUPPKEY        ││          Filters:         ││                           │
│         LO_REVENUE        ││    S_REGION='ASIA' AND    ││          Filters:         │
│                           ││    S_REGION IS NOT NULL   ││  P_BRAND>='MFGR#2221' AND │
│                           ││                           ││  P_BRAND<='MFGR#2228' AND │
│                           ││                           ││     P_BRAND IS NOT NULL   │
│                           ││                           ││                           │
│       59920777 Rows       ││         4001 Rows         ││         6409 Rows         │
│          (x̄:0.425,cv:0.071s)          ││          (x̄:0.000,cv:0.000s)          ││          (x̄:0.010,cv:0.000s)          │
└───────────────────────────┘└───────────────────────────┘└───────────────────────────┘
