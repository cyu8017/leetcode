// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        Map<String, List<String>> groups = new LinkedHashMap<>();

        for (String text : strings) {
            String key;
            if (text.isEmpty()) {
                key = "";
            } else {
                int base = text.charAt(0);
                StringBuilder builder = new StringBuilder();
                for (int index = 0; index < text.length(); index++) {
                    if (index > 0) {
                        builder.append(',');
                    }
                    builder.append((text.charAt(index) - base + 26) % 26);
                }
                key = builder.toString();
            }
            groups.computeIfAbsent(key, ignored -> new ArrayList<>()).add(text);
        }

        return new ArrayList<>(groups.values());
    }
}
