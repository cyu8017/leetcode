// LeetCode 2051 - The Category of Each Member in the Store
// https://leetcode.com/problems/the-category-of-each-member-in-the-store/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    m.member_id,\n"
    "    m.name,\n"
    "    CASE\n"
    "        WHEN COUNT(v.visit_id) = 0 THEN 'Bronze'\n"
    "        WHEN 100 * COUNT(p.charged_amount) / COUNT(v.visit_id) >= 80 THEN 'Diamond'\n"
    "        WHEN 100 * COUNT(p.charged_amount) / COUNT(v.visit_id) >= 50 THEN 'Gold'\n"
    "        ELSE 'Silver'\n"
    "    END AS category\n"
    "FROM Members AS m\n"
    "LEFT JOIN Visits AS v ON m.member_id = v.member_id\n"
    "LEFT JOIN Purchases AS p ON v.visit_id = p.visit_id\n"
    "GROUP BY m.member_id, m.name\n";
