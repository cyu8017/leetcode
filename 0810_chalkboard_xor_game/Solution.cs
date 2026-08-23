// LeetCode 0810 - Chalkboard XOR Game
// https://leetcode.com/problems/chalkboard-xor-game/

public class Solution {
    public bool XorGame(int[] nums) {
        int x = 0;
        foreach (int num in nums) x ^= num;
        return x == 0 || nums.Length % 2 == 0;
    }
}
