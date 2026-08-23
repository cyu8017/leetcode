// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

public class Solution {
    public int ValueAfterKSeconds(int n, int k) {
        const int mod = 1000000007;
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = 1;
        while (k-- > 0) {
            for (int i = 1; i < n; i++) a[i] = (a[i] + a[i - 1]) % mod;
        }
        return a[n - 1];
    }
}
