// LeetCode 3058 - Friends With No Mutual Friends
// https://leetcode.com/problems/friends-with-no-mutual-friends/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT user_id1, user_id2 FROM Friends\n"
    "        UNION ALL\n"
    "        SELECT user_id2, user_id1 FROM Friends\n"
    "    )\n"
    "SELECT user_id1, user_id2\n"
    "FROM Friends\n"
    "WHERE\n"
    "    (user_id1, user_id2) NOT IN (\n"
    "        SELECT t1.user_id1, t2.user_id1\n"
    "        FROM\n"
    "            T AS t1\n"
    "            JOIN T AS t2 ON t1.user_id2 = t2.user_id2\n"
    "    )\n"
    "ORDER BY 1, 2;\n";
