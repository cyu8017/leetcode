// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

class Solution {
    public boolean xorGame(int[] nums) {
        int x = 0;
        for (int num : nums) x ^= num;
        return x == 0 || nums.length % 2 == 0;
    }
}
