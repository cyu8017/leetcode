// LeetCode 0260 - Single Number III
// https://leetcode.com/problems/single-number-iii/

class Solution {
    public int[] singleNumber(int[] nums) {
        int xorAll = 0;
        for (int num : nums) {
            xorAll ^= num;
        }
        int diff = xorAll & -xorAll;
        int first = 0;
        int second = 0;
        for (int num : nums) {
            if ((num & diff) != 0) {
                first ^= num;
            } else {
                second ^= num;
            }
        }
        return new int[] { first, second };
    }
}
