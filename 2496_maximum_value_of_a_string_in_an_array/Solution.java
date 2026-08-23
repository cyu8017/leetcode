// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

class Solution {
    public int maximumValue(String[] strs) {
        int ans = 0;
        for (String s : strs) {
            boolean allDigit = true;
            int val = 0;
            for (char c : s) {
                if (c < '0' || c > '9') {
                    allDigit = false;
                    break;
                }
                val = val * 10 + (c - '0');
            }
            if (!allDigit) val = s.length();
            if (val > ans) ans = val;
        }
        return ans;
    }
}
