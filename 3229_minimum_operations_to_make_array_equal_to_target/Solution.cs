// LeetCode 3229 - Minimum Operations to Make Array Equal to Target
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

public class Solution {
    public long MinimumOperations(int[] nums, int[] target) {
        int Absv(int x) => x < 0 ? -x : x;
        long f = Absv(target[0] - nums[0]);
        for (int i = 1; i < target.Length; i++) {
            int x = target[i] - nums[i];
            int y = target[i - 1] - nums[i - 1];
            if ((long)x * y > 0) {
                int d = Absv(x) - Absv(y);
                if (d > 0) f += d;
            } else {
                f += Absv(x);
            }
        }
        return f;
    }
}
