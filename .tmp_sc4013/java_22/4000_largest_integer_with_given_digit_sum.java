// CONFIG class=Solution method=largestInteger types=None
// LeetCode 4000 - Largest Integer With Given Digit Sum
// https://leetcode.com/problems/largest-integer-with-given-digit-sum/

class Solution {
    public int largestInteger(int n, int s) {
        if (n * 9 < s) return -1;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x = s < 9 ? s : 9;
            ans = ans * 10 + x;
            s -= x;
        }
        return ans;
    }
}
