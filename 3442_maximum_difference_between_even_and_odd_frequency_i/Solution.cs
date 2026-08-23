// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

public class Solution {
    public int MaxDifference(string s) {
        int[] freq = new int[26];
        foreach (char c in s) freq[c - 'a']++;
        int maxOdd = 0, minEven = 1000000000;
        foreach (int f in freq) {
            if (f == 0) continue;
            if (f % 2 == 1) {
                if (f > maxOdd) maxOdd = f;
            } else if (f < minEven) minEven = f;
        }
        return maxOdd - minEven;
    }
}
