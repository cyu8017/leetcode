// LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
// https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

public class Solution {
    public string ModifyString(string s) {
        char[] chars = s.ToCharArray();
        for (int i = 0; i < chars.Length; i++) {
            if (chars[i] == '?') {
                foreach (char c in "abc") {
                    if ((i == 0 || chars[i - 1] != c) && (i + 1 == chars.Length || chars[i + 1] != c)) {
                        chars[i] = c;
                        break;
                    }
                }
            }
        }
        return new string(chars);
    }
}
