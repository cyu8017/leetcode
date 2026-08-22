// LeetCode 1990 - Count the Number of Experiments
// https://leetcode.com/problems/count-the-number-of-experiments/

const char* QUERY =
    "\n"
    "WITH\n"
    "    P AS (\n"
    "        SELECT 'Android' AS platform\n"
    "        UNION SELECT 'IOS'\n"
    "        UNION SELECT 'Web'\n"
    "    ),\n"
    "    Exp AS (\n"
    "        SELECT 'Reading' AS experiment_name\n"
    "        UNION SELECT 'Sports'\n"
    "        UNION SELECT 'Programming'\n"
    "    ),\n"
    "    T AS (\n"
    "        SELECT * FROM P, Exp\n"
    "    )\n"
    "SELECT platform, experiment_name, COUNT(experiment_id) AS num_experiments\n"
    "FROM T AS t\n"
    "LEFT JOIN Experiments USING (platform, experiment_name)\n"
    "GROUP BY 1, 2\n";
