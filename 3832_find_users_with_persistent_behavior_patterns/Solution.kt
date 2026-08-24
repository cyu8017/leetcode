// LeetCode 3832 - Find Users With Persistent Behavior Patterns
// https://leetcode.com/problems/find-users-with-persistent-behavior-patterns/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    daily_counts AS (\n" +
            "        -- Step 1: Filter user dates with exactly one record per day (meeting the requirement of \"exactly one action per day\")\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            action_date,\n" +
            "            action,\n" +
            "            COUNT(*) OVER (PARTITION BY user_id, action_date) AS cnt\n" +
            "        FROM activity\n" +
            "    ),\n" +
            "    filtered_activity AS (\n" +
            "        -- Step 2: Filter out data with multiple actions on the same day\n" +
            "        SELECT user_id, action_date, action\n" +
            "        FROM daily_counts\n" +
            "        WHERE cnt = 1\n" +
            "    ),\n" +
            "    streak_groups AS (\n" +
            "        -- Step 3: Group consecutive dates using the method of subtracting row number from date\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            action,\n" +
            "            action_date,\n" +
            "            DATE_SUB(\n" +
            "                action_date,\n" +
            "                INTERVAL ROW_NUMBER() OVER (\n" +
            "                    PARTITION BY user_id, action\n" +
            "                    ORDER BY action_date\n" +
            "                ) DAY\n" +
            "            ) AS grp\n" +
            "        FROM filtered_activity\n" +
            "    ),\n" +
            "    streak_summary AS (\n" +
            "        -- Step 4: Calculate the length of each consecutive segment and only keep records with length >= 5\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            action,\n" +
            "            COUNT(*) AS streak_length,\n" +
            "            MIN(action_date) AS start_date,\n" +
            "            MAX(action_date) AS end_date,\n" +
            "            -- Sort different streaks for each user to facilitate getting the maximum value later\n" +
            "            ROW_NUMBER() OVER (\n" +
            "                PARTITION BY user_id\n" +
            "                ORDER BY COUNT(*) DESC\n" +
            "            ) AS rnk\n" +
            "        FROM streak_groups\n" +
            "        GROUP BY user_id, action, grp\n" +
            "        HAVING streak_length >= 5\n" +
            "    )\n" +
            "-- Step 5: Extract the longest record for each qualified user and sort\n" +
            "SELECT user_id, action, streak_length, start_date, end_date\n" +
            "FROM streak_summary\n" +
            "WHERE rnk = 1\n" +
            "ORDER BY streak_length DESC, user_id ASC;"
    }
}
