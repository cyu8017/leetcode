// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

public class Solution {
    public long CountNoZeroPairs(long n) {
        string s = n.ToString();
        int m = s.Length;
        int[] digits = new int[m + 1];
        for (int i = 0; i < m; i++) digits[i] = s[m - 1 - i] - '0';

        long[,,] dp = new long[2, 2, 2];
        dp[0, 1, 1] = 1;

        for (int pos = 0; pos < m + 1; pos++) {
            long[,,] ndp = new long[2, 2, 2];
            int target = digits[pos];
            for (int carry = 0; carry <= 1; carry++) {
                for (int aliveA = 0; aliveA <= 1; aliveA++) {
                    for (int aliveB = 0; aliveB <= 1; aliveB++) {
                        long ways = dp[carry, aliveA, aliveB];
                        if (ways == 0) continue;
                        int[,] A = new int[10, 2];
                        int aLen = 0;
                        if (aliveA == 1) {
                            for (int d = 1; d <= 9; d++) {
                                A[aLen, 0] = d; A[aLen, 1] = 1; aLen++;
                            }
                            if (pos > 0) { A[aLen, 0] = 0; A[aLen, 1] = 0; aLen++; }
                        } else {
                            A[0, 0] = 0; A[0, 1] = 0; aLen = 1;
                        }
                        int[,] B = new int[10, 2];
                        int bLen = 0;
                        if (aliveB == 1) {
                            for (int d = 1; d <= 9; d++) {
                                B[bLen, 0] = d; B[bLen, 1] = 1; bLen++;
                            }
                            if (pos > 0) { B[bLen, 0] = 0; B[bLen, 1] = 0; bLen++; }
                        } else {
                            B[0, 0] = 0; B[0, 1] = 0; bLen = 1;
                        }
                        for (int ai = 0; ai < aLen; ai++) {
                            int da = A[ai, 0], na = A[ai, 1];
                            for (int bi = 0; bi < bLen; bi++) {
                                int db = B[bi, 0], nb = B[bi, 1];
                                int sum = da + db + carry;
                                if (sum % 10 != target) continue;
                                int ncarry = sum / 10;
                                ndp[ncarry, na, nb] += ways;
                            }
                        }
                    }
                }
            }
            for (int c = 0; c < 2; c++)
                for (int a = 0; a < 2; a++)
                    for (int b = 0; b < 2; b++)
                        dp[c, a, b] = ndp[c, a, b];
        }
        return dp[0, 0, 0];
    }
}
