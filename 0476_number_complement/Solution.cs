// LeetCode 0476 - Number Complement
// https://leetcode.com/problems/number-complement/

public class Solution {
    public int FindComplement(int num) {
        int mask = num;
        mask |= mask >> 1;
        mask |= mask >> 2;
        mask |= mask >> 4;
        mask |= mask >> 8;
        mask |= mask >> 16;
        return num ^ mask;
    }
}
