// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

public class Solution {
    public bool HaveConflict(string[] event1, string[] event2) {
        return event1[0].CompareTo(event2[1]) <= 0 && event2[0].CompareTo(event1[1]) <= 0;
    }
}
