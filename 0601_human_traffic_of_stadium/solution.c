// LeetCode 0601 - Human Traffic of Stadium
// https://leetcode.com/problems/human-traffic-of-stadium/

const char* QUERY =
    "\n"
    "WITH busy AS (\n"
    "    SELECT\n"
    "        id,\n"
    "        visit_date,\n"
    "        people,\n"
    "        id - ROW_NUMBER() OVER (ORDER BY id) AS grp\n"
    "    FROM Stadium\n"
    "    WHERE people >= 100\n"
    "),\n"
    "valid_groups AS (\n"
    "    SELECT grp\n"
    "    FROM busy\n"
    "    GROUP BY grp\n"
    "    HAVING COUNT(*) >= 3\n"
    ")\n"
    "SELECT id, visit_date, people\n"
    "FROM busy\n"
    "WHERE grp IN (SELECT grp FROM valid_groups)\n"
    "ORDER BY visit_date\n";
