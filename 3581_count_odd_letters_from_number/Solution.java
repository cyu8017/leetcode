// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countOddLetters(int n) {
        Map<Integer, String> d = new HashMap<>();
        d.put(0, "zero"); d.put(1, "one"); d.put(2, "two"); d.put(3, "three"); d.put(4, "four");
        d.put(5, "five"); d.put(6, "six"); d.put(7, "seven"); d.put(8, "eight"); d.put(9, "nine");
        int mask = 0;
        while (n > 0) {
            for (char c : d.get(n % 10).toCharArray()) mask ^= 1 << (c - 'a');
            n /= 10;
        }
        return Integer.bitCount(mask);
    }
}
