// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find_nth_smallest_integer_with_k_one_bits/

class Solution {
    private static final int MX = 50;
    private static final long[][] C = new long[MX][MX + 1];
    static {
        for (int i = 0; i < MX; i++) {
            C[i][0] = 1;
            for (int j = 1; j <= i; j++) C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
        }
    }

    public long nthSmallest(long n, int k) {
        long ans = 0;
        for (int i = 49; i >= 0; i--) {
            if (n > C[i][k]) {
                n -= C[i][k];
                ans |= 1L << i;
                k--;
                if (k == 0) break;
            }
        }
        return ans;
    }
}
