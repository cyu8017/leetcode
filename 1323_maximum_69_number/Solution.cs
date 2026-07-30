// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

public class Solution {
    public int Maximum69Number(int num) {
        char[] chars = num.ToString().ToCharArray();
        for (int i = 0; i < chars.Length; i++) {
            if (chars[i] == '6') { chars[i] = '9'; break; }
        }
        return int.Parse(new string(chars));
    }
}
