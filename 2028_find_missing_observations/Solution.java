// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int sum = 0;
        for (int r : rolls) sum += r;
        int remain = mean * (rolls.length + n) - sum;
        if (remain < n || remain > 6 * n) return new int[0];
        int[] ans = new int[n];
        int baseVal = remain / n, extra = remain % n;
        for (int i = 0; i < n; i++) ans[i] = baseVal + (i < extra ? 1 : 0);
        return ans;
    }
}
