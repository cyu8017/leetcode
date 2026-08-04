// LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
// https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

import java.util.*;

class Solution {
    public String modifyString(String s) {
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '?') {
                for (char c = 'a'; c <= 'c'; c++) {
                    if ((i == 0 || chars[i - 1] != c)
                            && (i + 1 == chars.length || chars[i + 1] != c)) {
                        chars[i] = c;
                        break;
                    }
                }
            }
        }
        return new String(chars);
    }
}
