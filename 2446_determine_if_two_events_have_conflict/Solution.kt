// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

class Solution {
    fun haveConflict(event1: Array<String>, event2: Array<String>): Boolean {
        return event1[0] <= event2[1] && event2[0] <= event1[1]
    }
}
