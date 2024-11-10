┌─────────────────────────────────────┐
│┌───────────────────────────────────┐│
││    Query Profiling Information    ││
│└───────────────────────────────────┘│
└─────────────────────────────────────┘
EXPLAIN ANALYZE  SELECT     sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS REVENUE FROM     lineorder,     date WHERE     LO_ORDERDATE = D_DATEKEY     AND D_YEAR = 1993     AND LO_DISCOUNT BETWEEN 1 AND 3     AND LO_QUANTITY < 25;
┌────────────────────────────────────────────────┐
│┌──────────────────────────────────────────────┐│
││              Total Time: x̄:0.072,cv:0.051s             ││
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
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│      EXPLAIN_ANALYZE      │
│    ────────────────────   │
│           0 Rows          │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│    UNGROUPED_AGGREGATE    │
│    ────────────────────   │
│    Aggregates: sum(#0)    │
│                           │
│           1 Rows          │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         PROJECTION        │
│    ────────────────────   │
│  (LO_EXTENDEDPRICE * CAST │
│ (LO_DISCOUNT AS INTEGER)) │
│                           │
│        1193001 Rows       │
│          (x̄:0.000,cv:0.000s)          │
└─────────────┬─────────────┘
┌─────────────┴─────────────┐
│         HASH_JOIN         │
│    ────────────────────   │
│      Join Type: INNER     │
│                           │
│        Conditions:        │
│  LO_ORDERDATE = D_DATEKEY │
│                           ├──────────────┐
│   Build Min: 1992-01-02   │              │
│   Build Max: 1998-12-30   │              │
│                           │              │
│        1193001 Rows       │              │
│          (x̄:0.060,cv:0.059s)          │              │
└─────────────┬─────────────┘              │
┌─────────────┴─────────────┐┌─────────────┴─────────────┐
│         TABLE_SCAN        ││         TABLE_SCAN        │
│    ────────────────────   ││    ────────────────────   │
│         lineorder         ││            date           │
│                           ││                           │
│        Projections:       ││        Projections:       │
│        LO_ORDERDATE       ││         D_DATEKEY         │
│        LO_DISCOUNT        ││                           │
│      LO_EXTENDEDPRICE     ││          Filters:         │
│                           ││ D_YEAR=1993 AND D_YEAR IS │
│          Filters:         ││          NOT NULL         │
│     LO_DISCOUNT>=1 AND    ││                           │
│     LO_DISCOUNT<=3 AND    ││                           │
│   LO_DISCOUNT IS NOT NULL ││                           │
│     LO_QUANTITY<25 AND    ││                           │
│   LO_QUANTITY IS NOT NULL ││                           │
│                           ││                           │
│        1193001 Rows       ││          365 Rows         │
│          (x̄:0.483,cv:0.051s)          ││          (x̄:0.000,cv:0.000s)          │
└───────────────────────────┘└───────────────────────────┘
