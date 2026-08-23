// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

class Solution {
    public int valueAfterKSeconds(int n, int k) {
        final int mod = 1000000007;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = 1;
        while (k-- > 0) {
            for (int i = 1; i < n; i++) a[i] = (a[i] + a[i - 1]) % mod;
        }
        return a[n - 1];
    }
}
