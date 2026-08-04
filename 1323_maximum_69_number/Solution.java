// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

class Solution {
    public int maximum69Number(int num) {
        char[] chars = num.ToString().toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '6') { chars[i] = '9'; break; }
        }
        return Integer.parseInt(new String(chars));
    }
}
