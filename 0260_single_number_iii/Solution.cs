// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

public class Solution {
    public int[] SingleNumber(int[] nums) {
        int xorAll = 0;
        foreach (int num in nums) {
            xorAll ^= num;
        }
        int diff = xorAll & -xorAll;
        int first = 0;
        int second = 0;
        foreach (int num in nums) {
            if ((num & diff) != 0) {
                first ^= num;
            } else {
                second ^= num;
            }
        }
        return new int[] { first, second };
    }
}
