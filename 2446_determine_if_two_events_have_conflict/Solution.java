// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

class Solution {
    public boolean haveConflict(String[] event1, String[] event2) {
        return Integer.compare(event1[0], event2[1]) <= 0 && Integer.compare(event2[0], event1[1]) <= 0;
    }
}
