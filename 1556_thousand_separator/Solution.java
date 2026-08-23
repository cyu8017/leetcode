// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/

import java.util.*;

class Solution {
    public String thousandSeparator(int n) {
        String s = String.valueOf(n);
        List<String> parts = new ArrayList<>();
        while (!s.isEmpty()) {
            int start = Math.max(0, s.length() - 3);
            parts.add(s.substring(start));
            s = s.substring(0, start);
        }
        Collections.reverse(parts);
        return String.join(".", parts);
    }
}
