// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String licenseKeyFormatting(String s, int k) {
        List<Character> chars = new ArrayList<>();
        for (char ch : s.toCharArray()) {
            if (ch != '-') {
                chars.add(Character.toUpperCase(ch));
            }
        }
        if (chars.isEmpty()) {
            return "";
        }
        int firstLen = chars.size() % k;
        if (firstLen == 0) {
            firstLen = k;
        }
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < firstLen; i++) {
            result.append(chars.get(i));
        }
        for (int i = firstLen; i < chars.size(); i += k) {
            result.append('-');
            for (int j = i; j < i + k; j++) {
                result.append(chars.get(j));
            }
        }
        return result.toString();
    }
}
