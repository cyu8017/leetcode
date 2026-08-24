// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

class Solution {
    func haveConflict(_ event1: [String], _ event2: [String]) -> Bool {
        event1[0] <= event2[1] && event2[0] <= event1[1]
    }
}
