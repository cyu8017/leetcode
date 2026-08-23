// LeetCode 2498 - Frog Jump II
// https://leetcode.com/problems/frog-jump-ii/

public class Solution {
    public int MaxJump(int[] stones) {
        int ans = stones[1] - stones[0];
        for (int i = 2; i < stones.Length; i++) {
            int diff = stones[i] - stones[i - 2];
            if (diff > ans) ans = diff;
        }
        return ans;
    }
}
