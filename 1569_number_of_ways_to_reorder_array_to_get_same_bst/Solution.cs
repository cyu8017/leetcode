// LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    private const int MOD = 1000000007;

    public int NumOfWays(int[] nums) {
        int n = nums.Length;
        long[,] choose = new long[n + 1, n + 1];
        for (int i = 0; i <= n; i++) {
            choose[i, 0] = choose[i, i] = 1;
            for (int j = 1; j < i; j++)
                choose[i, j] = (choose[i - 1, j - 1] + choose[i - 1, j]) % MOD;
        }

        long Ways(List<int> values) {
            if (values.Count < 3) return 1;
            int root = values[0];
            var left = values.Skip(1).Where(x => x < root).ToList();
            var right = values.Skip(1).Where(x => x > root).ToList();
            return choose[values.Count - 1, left.Count] * Ways(left) % MOD * Ways(right) % MOD;
        }

        return (int)((Ways(nums.ToList()) - 1 + MOD) % MOD);
    }
}
