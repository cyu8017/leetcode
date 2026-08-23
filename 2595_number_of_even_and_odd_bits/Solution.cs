// LeetCode 2595 - Number of Even and Odd Bits
// https://leetcode.com/problems/number-of-even-and-odd-bits/

public class Solution {
    public int[] EvenOddBit(int n) {
        int even = 0, odd = 0, i = 0;
        while (n > 0) {
            if ((n & 1) != 0) {
                if (i % 2 == 0) even++;
                else odd++;
            }
            n >>= 1;
            i++;
        }
        return new[] { even, odd };
    }
}
