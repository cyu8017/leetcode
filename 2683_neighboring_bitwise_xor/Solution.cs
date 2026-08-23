// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/

public class Solution {
    public bool DoesValidArrayExist(int[] derived) {
        int x = 0;
        foreach (int v in derived) x ^= v;
        return x == 0;
    }
}
