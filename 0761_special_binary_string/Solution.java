// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

import java.util.*;

class Solution {
    public String makeLargestSpecial(String s) {
        List<String> parts = new ArrayList<>();
        int balance = 0, start = 0;
        for (int i = 0; i < s.length(); i++) {
            balance += s.charAt(i) == '1' ? 1 : -1;
            if (balance == 0) {
                parts.add("1" + makeLargestSpecial(s.substring(start + 1, i)) + "0");
                start = i + 1;
            }
        }
        parts.sort((a, b) -> b.compareTo(a));
        StringBuilder result = new StringBuilder();
        for (String part : parts) result.append(part);
        return result.toString();
    }
}
