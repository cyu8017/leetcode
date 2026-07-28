// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public String[] expand(String s) {
        List<List<String>> groups = new ArrayList<>();
        int i = 0;
        while (i < s.length()) {
            if (s.charAt(i) == '{') {
                int j = i + 1;
                while (s.charAt(j) != '}') {
                    j++;
                }
                String[] parts = s.substring(i + 1, j).split(",");
                Arrays.sort(parts);
                groups.add(Arrays.asList(parts));
                i = j + 1;
            } else {
                groups.add(List.of(String.valueOf(s.charAt(i))));
                i++;
            }
        }
        List<String> ans = new ArrayList<>();
        ans.add("");
        for (List<String> group : groups) {
            List<String> next = new ArrayList<>();
            for (String prefix : ans) {
                for (String ch : group) {
                    next.add(prefix + ch);
                }
            }
            ans = next;
        }
        return ans.toArray(new String[0]);
    }
}
