// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

public class Solution {
    public int MaxScore(int[] nums) {
        int n = nums.Length;
        var memo = new int[1 << n];
        Array.Fill(memo, -1);

        int Gcd(int a, int b) {
            while (b != 0) {
                int t = a % b;
                a = b;
                b = t;
            }
            return a;
        }

        int Popcount(int x) {
            int count = 0;
            while (x != 0) {
                x &= x - 1;
                count++;
            }
            return count;
        }

        int Dp(int mask) {
            if (mask == (1 << n) - 1) return 0;
            if (memo[mask] != -1) return memo[mask];
            int step = Popcount(mask) / 2 + 1;
            int best = 0;
            for (int i = 0; i < n; i++) {
                if ((mask >> i & 1) == 1) continue;
                for (int j = i + 1; j < n; j++) {
                    if ((mask >> j & 1) == 1) continue;
                    best = Math.Max(
                        best,
                        step * Gcd(nums[i], nums[j]) + Dp(mask | (1 << i) | (1 << j))
                    );
                }
            }
            memo[mask] = best;
            return best;
        }

        return Dp(0);
    }
}
