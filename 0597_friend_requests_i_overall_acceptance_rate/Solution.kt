// LeetCode 0597 - Friend Requests I Overall Acceptance Rate
// https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    ROUND(\n" +
            "        IFNULL(\n" +
            "            (\n" +
            "                SELECT COUNT(*)\n" +
            "                FROM (\n" +
            "                    SELECT DISTINCT requester_id, accepter_id\n" +
            "                    FROM RequestAccepted\n" +
            "                ) accepted\n" +
            "            ) / (\n" +
            "                SELECT COUNT(*)\n" +
            "                FROM (\n" +
            "                    SELECT DISTINCT sender_id, send_to_id\n" +
            "                    FROM FriendRequest\n" +
            "                ) requested\n" +
            "            ),\n" +
            "            0\n" +
            "        ),\n" +
            "        2\n" +
            "    ) AS accept_rate"
    }
}
