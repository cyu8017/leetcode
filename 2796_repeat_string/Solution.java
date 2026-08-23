// LeetCode 2796 - Repeat String
// https://leetcode.com/problems/repeat-string/
// JS-only problem; C# stand-in.

class Solution {
    public String replicate(String str, int times) {
        if (times <= 0) return "";
        var sb = new StringBuilder(str.length() * times);
        for (int i = 0; i < times; i++) sb.append(str);
        return sb.toString();
    }
}
