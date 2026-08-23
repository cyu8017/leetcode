// LeetCode 3847 - Find The Score Difference In A Game
// https://leetcode.com/problems/find-the-score-difference-in-a-game/

public class Solution {
    public int ScoreDifference(int[] nums) {
        int ans = 0, k = 1;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] % 2 != 0) k = -k;
            if (i % 6 == 5) k = -k;
            ans += k * nums[i];
        }
        return ans;
    }
}
