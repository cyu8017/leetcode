// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

public class Solution {
    int OpsToZero(int x) {
        int ops = 0;
        while (x > 0) { x /= 4; ops++; }
        return ops;
    }

    public long MinOperations(int[][] queries) {
        long ans = 0;
        foreach (var q in queries) {
            int l = q[0], r = q[1];
            long sum = 0;
            for (int x = l; x <= r; x++) sum += OpsToZero(x);
            ans += (sum + 1) / 2;
        }
        return ans;
    }
}
