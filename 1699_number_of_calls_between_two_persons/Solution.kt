// LeetCode 1699 - Number Of Calls Between Two Persons
// https://leetcode.com/problems/number-of-calls-between-two-persons/

class Solution {
    companion object {
        const val QUERY = "SELECT LEAST(from_id,to_id) person1, GREATEST(from_id,to_id) person2,\n" +
            "COUNT(*) call_count, SUM(duration) total_duration\n" +
            "FROM Calls GROUP BY LEAST(from_id,to_id), GREATEST(from_id,to_id)"
    }
}
