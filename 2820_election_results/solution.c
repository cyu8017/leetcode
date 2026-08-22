// LeetCode 2820 - Election Results
// https://leetcode.com/problems/election-results/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT candidate, SUM(vote) AS tot\n"
    "        FROM\n"
    "            (\n"
    "                SELECT\n"
    "                    candidate,\n"
    "                    1 / (COUNT(candidate) OVER (PARTITION BY voter)) AS vote\n"
    "                FROM Votes\n"
    "                WHERE candidate IS NOT NULL\n"
    "            ) AS t\n"
    "        GROUP BY 1\n"
    "    ),\n"
    "    P AS (\n"
    "        SELECT\n"
    "            candidate,\n"
    "            RANK() OVER (ORDER BY tot DESC) AS rk\n"
    "        FROM T\n"
    "    )\n"
    "SELECT candidate\n"
    "FROM P\n"
    "WHERE rk = 1\n"
    "ORDER BY 1\n";
