// LeetCode 3232 - Find if Digit Game Can Be Won
// https://leetcode.com/problems/find-if-digit-game-can-be-won/

public class Solution {
    public bool CanAliceWin(int[] nums) {
        int a = 0, b = 0;
        foreach (int x in nums) {
            if (x < 10) a += x;
            else b += x;
        }
        return a != b;
    }
}
