// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public boolean isValid(String code) {
        Deque<String> stack = new ArrayDeque<>();
        int i = 0;
        int n = code.length();

        while (i < n) {
            if (code.startsWith("<![CDATA[", i)) {
                if (stack.isEmpty()) {
                    return false;
                }
                int j = code.indexOf("]]>", i + 9);
                if (j < 0) {
                    return false;
                }
                i = j + 3;
            } else if (code.startsWith("</", i)) {
                int j = code.indexOf('>', i + 2);
                if (j < 0) {
                    return false;
                }
                String tag = code.substring(i + 2, j);
                if (stack.isEmpty() || !stack.peek().equals(tag)) {
                    return false;
                }
                stack.pop();
                i = j + 1;
                if (stack.isEmpty() && i < n) {
                    return false;
                }
            } else if (code.charAt(i) == '<') {
                int j = code.indexOf('>', i + 1);
                if (j < 0) {
                    return false;
                }
                String tag = code.substring(i + 1, j);
                if (tag.isEmpty() || tag.length() > 9) {
                    return false;
                }
                for (int k = 0; k < tag.length(); ++k) {
                    char ch = tag.charAt(k);
                    if (ch < 'A' || ch > 'Z') {
                        return false;
                    }
                }
                stack.push(tag);
                i = j + 1;
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                ++i;
            }
        }
        return stack.isEmpty();
    }
}
