// LeetCode 3224 - Minimum Array Changes to Make Differences Equal
// https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/

class Solution {
    public int minChanges(int[] nums, int k) {
        int[] d = new int[k + 2];
        int n = nums.length;
        for (int i = 0; i < n / 2; i++) {
            int x = nums[i], y = nums[n - 1 - i];
            if (x > y) { int t = x; x = y; y = t; }
            d[0] += 1;
            d[y - x] -= 1;
            d[y - x + 1] += 1;
            int mx = Math.max(y, k - x);
            d[mx + 1] -= 1;
            d[mx + 1] += 2;
        }
        int ans = n, s = 0;
        for (int x : d) {
            s += x;
            ans = Math.min(ans, s);
        }
        return ans;
    }
}
