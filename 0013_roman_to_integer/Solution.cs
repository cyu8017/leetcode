// LeetCode 0013 - Roman to Integer
// https://leetcode.com/problems/roman-to-integer/

public class Solution {
    public int RomanToInt(string s) {
        var values = new Dictionary<char, int> {
            ['I'] = 1,
            ['V'] = 5,
            ['X'] = 10,
            ['L'] = 50,
            ['C'] = 100,
            ['D'] = 500,
            ['M'] = 1000,
        };

        int total = 0;
        int prev = 0;
        for (int i = s.Length - 1; i >= 0; i--) {
            int curr = values[s[i]];
            if (curr < prev) {
                total -= curr;
            } else {
                total += curr;
            }
            prev = curr;
        }

        return total;
    }
}
