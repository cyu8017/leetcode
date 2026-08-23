// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

import java.util.*;

class Solution {
    public List<String> removeComments(String[] source) {
        List<String> result = new ArrayList<>();
        StringBuilder buffer = new StringBuilder();
        boolean inBlock = false;
        for (String line : source) {
            int i = 0;
            while (i < line.length()) {
                if (inBlock) {
                    if (i + 1 < line.length() && line.charAt(i) == '*' && line.charAt(i + 1) == '/') {
                        inBlock = false;
                        i += 2;
                    } else i++;
                } else if (i + 1 < line.length() && line.charAt(i) == '/' && line.charAt(i + 1) == '*') {
                    inBlock = true;
                    i += 2;
                } else if (i + 1 < line.length() && line.charAt(i) == '/' && line.charAt(i + 1) == '/') break;
                else buffer.append(line.charAt(i++));
            }
            if (!inBlock && buffer.length() > 0) {
                result.add(buffer.toString());
                buffer.setLength(0);
            }
        }
        return result;
    }
}
