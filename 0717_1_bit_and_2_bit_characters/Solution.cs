// LeetCode 0717 - 1-bit and 2-bit Characters
// https://leetcode.com/problems/1-bit-and-2-bit-characters/

public class Solution {
    public bool IsOneBitCharacter(int[] bits) {
        int i = 0, n = bits.Length;
        while (i < n - 1) i += bits[i] == 1 ? 2 : 1;
        return i == n - 1;
    }
}
