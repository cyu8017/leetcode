// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private Map<String, String> mp;

    public String applySubstitutions(List<List<String>> replacements, String text) {
        mp = new HashMap<>();
        for (List<String> r : replacements) mp.put(r.get(0), r.get(1));
        return resolve(text);
    }

    private String resolve(String s) {
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < s.length(); ) {
            if (s.charAt(i) == '%') {
                int j = i + 1;
                while (j < s.length() && s.charAt(j) != '%') j++;
                String key = s.substring(i + 1, j);
                out.append(resolve(mp.get(key)));
                i = j + 1;
            } else {
                out.append(s.charAt(i));
                i++;
            }
        }
        return out.toString();
    }
}
