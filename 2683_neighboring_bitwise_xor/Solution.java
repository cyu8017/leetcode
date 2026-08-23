// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int x = 0;
        for (int v : derived) x ^= v;
        return x == 0;
    }
}
