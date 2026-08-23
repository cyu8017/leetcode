// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

public class Solution {
    public int MaximumValue(string[] strs) {
        int ans = 0;
        foreach (string s in strs) {
            bool allDigit = true;
            int val = 0;
            foreach (char c in s) {
                if (c < '0' || c > '9') {
                    allDigit = false;
                    break;
                }
                val = val * 10 + (c - '0');
            }
            if (!allDigit) val = s.Length;
            if (val > ans) ans = val;
        }
        return ans;
    }
}
