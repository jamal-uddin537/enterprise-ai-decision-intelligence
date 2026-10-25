-- Phase 1 SQL practice on the `wine` table (created in notebooks/01_intro_data_analysis.ipynb).
-- Run each query, predict the result first, then check.

-- 1. Basics: SELECT, WHERE, ORDER BY, LIMIT
SELECT cultivar, alcohol, color_intensity
FROM wine
WHERE alcohol > 13.5
ORDER BY alcohol DESC
LIMIT 10;

-- 2. Aggregation: GROUP BY + HAVING (HAVING filters groups, WHERE filters rows)
SELECT cultivar,
       COUNT(*)              AS n_wines,
       ROUND(AVG(alcohol),2) AS avg_alcohol
FROM wine
GROUP BY cultivar
HAVING COUNT(*) > 50;

-- 3. CASE: build a category from a number
SELECT CASE WHEN alcohol >= 13 THEN 'high' ELSE 'normal' END AS alcohol_band,
       COUNT(*) AS n
FROM wine
GROUP BY alcohol_band;

-- 4. CTE (WITH): compute per-group average, then compare each row to it
WITH group_avg AS (
    SELECT cultivar, AVG(alcohol) AS avg_alcohol
    FROM wine
    GROUP BY cultivar
)
SELECT w.cultivar, w.alcohol, ROUND(g.avg_alcohol, 2) AS group_avg,
       ROUND(w.alcohol - g.avg_alcohol, 2)           AS diff_from_group
FROM wine AS w
JOIN group_avg AS g USING (cultivar)
ORDER BY diff_from_group DESC
LIMIT 5;

-- 5. Window function: rank wines by alcohol within each cultivar
SELECT cultivar, alcohol,
       RANK() OVER (PARTITION BY cultivar ORDER BY alcohol DESC) AS rank_in_group
FROM wine
ORDER BY cultivar, rank_in_group;

-- EXERCISE: return only the top 3 wines per cultivar.
-- You cannot use rank_in_group in WHERE of the same query (window functions run after WHERE).
-- Hint: wrap query 5 in a CTE, then filter WHERE rank_in_group <= 3.
