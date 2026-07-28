// LeetCode 1009 - Complement of Base 10 Integer
// https://leetcode.com/problems/complement-of-base-10-integer/

public class Solution {
    public int BitwiseComplement(int n) {
        if (n == 0) return 1;
        int x = n, mask = 0;
        while (x > 0) {
            mask = (mask << 1) | 1;
            x >>= 1;
        }
        return n ^ mask;
    }
}
