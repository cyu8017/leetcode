// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

class Solution {
    public int[] diStringMatch(String s) {
        int lo = 0, hi = s.length();
        int[] ans = new int[s.length() + 1];
        int k = 0;
        for (char ch : s.toCharArray()) {
            if (ch == 'I') ans[k++] = lo++;
            else ans[k++] = hi--;
        }
        ans[k] = lo;
        return ans;
    }
}
