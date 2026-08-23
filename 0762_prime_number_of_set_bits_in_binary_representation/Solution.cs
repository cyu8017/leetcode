// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

using System.Collections.Generic;

public class Solution {
    public int CountPrimeSetBits(int left, int right) {
        var primes = new HashSet<int> { 2, 3, 5, 7, 11, 13, 17, 19 };
        int ans = 0;
        for (int num = left; num <= right; num++) {
            int bits = 0;
            for (int x = num; x > 0; x >>= 1) bits += x & 1;
            if (primes.Contains(bits)) ans++;
        }
        return ans;
    }
}
