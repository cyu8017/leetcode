// LeetCode 0798 - Smallest Rotation with Highest Score
// https://leetcode.com/problems/smallest-rotation-with-highest-score/

class Solution {
    public int bestRotation(int[] nums) {
        int n = nums.length;
        int[] change = new int[n];
        java.util.Arrays.fill(change, 1);
        for (int i = 0; i < n; i++) change[(i - nums[i] + 1 + n) % n] -= 1;
        for (int i = 1; i < n; i++) change[i] += change[i - 1];
        int best = 0;
        for (int i = 1; i < n; i++) if (change[i] > change[best]) best = i;
        return best;
    }
}
