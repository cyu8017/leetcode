// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution {
    public int maxDifference(String s) {
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;
        int maxOdd = 0, minEven = 1000000000;
        for (int f : freq) {
            if (f == 0) continue;
            if (f % 2 == 1) {
                if (f > maxOdd) maxOdd = f;
            } else if (f < minEven) minEven = f;
        }
        return maxOdd - minEven;
    }
}
