// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

import java.util.*;

class Solution {
    public int countPrimeSetBits(int left, int right) {
        Set<Integer> primes = new HashSet<>(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19));
        int ans = 0;
        for (int num = left; num <= right; num++) {
            int bits = Integer.bitCount(num);
            if (primes.contains(bits)) ans++;
        }
        return ans;
    }
}
