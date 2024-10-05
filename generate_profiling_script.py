queries = [
# single join on small dimensional table, filter by point and range. No group by, no order by 
"""
SELECT
    sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS REVENUE
FROM
    lineorder,
    date
WHERE
    LO_ORDERDATE = D_DATEKEY
    AND D_YEAR = 1993
    AND LO_DISCOUNT BETWEEN 1 AND 3
    AND LO_QUANTITY < 25;
"""
,
# many joins, two group bys (and a sum) and also order by.
"""
SELECT
    sum(LO_REVENUE),
    D_YEAR,
    P_BRAND
FROM
    lineorder,
    date,
    part,
    supplier
WHERE
    LO_ORDERDATE = D_DATEKEY
    AND LO_PARTKEY = P_PARTKEY
    AND LO_SUPPKEY = S_SUPPKEY
    AND P_CATEGORY = 'MFGR#12'
    AND S_REGION = 'AMERICA'
GROUP BY
    D_YEAR,
    P_BRAND
ORDER BY
    D_YEAR,
    P_BRAND;
"""
,
# many joins, group bys (and a sum), order bys AND range scans also 
"""
SELECT
    sum(LO_REVENUE),
    D_YEAR,
    P_BRAND
FROM
    lineorder,
    date,
    part,
    supplier
WHERE
    LO_ORDERDATE = D_DATEKEY
    AND LO_PARTKEY = P_PARTKEY
    AND LO_SUPPKEY = S_SUPPKEY
    AND P_BRAND BETWEEN
    'MFGR#2221' AND 'MFGR#2228'
    AND S_REGION = 'ASIA'
GROUP BY
    D_YEAR,
    P_BRAND
ORDER BY
    D_YEAR,
    P_BRAND;
"""
]

script = """
PRAGMA disable_object_cache;

SET profiling_mode = 'detailed';
PRAGMA ENABLE_PROFILING = 'query_tree_optimizer'; 
SET explain_output = 'all';

"""

# for t in [1, 4, 8]: # uncomment for thread_count experiment
for t in [8]: # only use 8 threads for second part of project where we profile different database sizes. 
    script += f"SET threads TO {t};\n"
    for q in range(3): 
        for i in range(50): 
            script += f".output outputs/hot_repetition/threadcount_{t}/q{q+1}/profile_{i}.md \n"
            script += "EXPLAIN ANALYZE "
            script += queries[q] 
            script += "\n"

with open("hot_repetitions.sql", "w") as outfile: 
    outfile.write(script)