// LeetCode 0597 - Friend Requests I Overall Acceptance Rate
// https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/

var QUERY = `SELECT
    ROUND(
        IFNULL(
            (
                SELECT COUNT(*)
                FROM (
                    SELECT DISTINCT requester_id, accepter_id
                    FROM RequestAccepted
                ) accepted
            ) / (
                SELECT COUNT(*)
                FROM (
                    SELECT DISTINCT sender_id, send_to_id
                    FROM FriendRequest
                ) requested
            ),
            0
        ),
        2
    ) AS accept_rate`;

module.exports = { QUERY };
