// LeetCode 1646 - Get Maximum in Generated Array
// https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution {
    public int getMaximumGenerated(int n) {
        if (n < 2) return n;
        int[] a = new int[n + 1];
        a[1] = 1;
        int ans = 1;
        for (int i = 2; i <= n; i++) {
            a[i] = i % 2 == 0 ? a[i / 2] : a[i / 2] + a[i / 2 + 1];
            ans = Math.max(ans, a[i]);
        }
        return ans;
    }
}
