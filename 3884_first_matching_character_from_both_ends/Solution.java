// LeetCode 3884 - First Matching Character From Both Ends
// https://leetcode.com/problems/first-matching-character-from-both-ends/

class Solution {
    public int firstMatchingIndex(String s) {
        int n = s.length();
        for (int i = 0; i < n / 2 + 1; i++) {
            if (s.charAt(i) == s.charAt(n - i - 1)) return i;
        }
        return -1;
    }
}
