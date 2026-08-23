// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String evaluate(String s, String[][] knowledge) {
        Map<String, String> lookup = new HashMap<>();
        for (String[] pair : knowledge) {
            lookup.put(pair[0], pair[1]);
        }
        return evaluateWithLookup(s, lookup);
    }

    public String evaluate(String s, char[][] knowledge) {
        String[][] converted = new String[knowledge.length][];
        for (int i = 0; i < knowledge.length; i++) {
            converted[i] = new String[knowledge[i].length];
            for (int j = 0; j < knowledge[i].length; j++) {
                converted[i][j] = String.valueOf(knowledge[i][j]);
            }
        }
        return evaluate(s, converted);
    }

    private String evaluateWithLookup(String s, Map<String, String> lookup) {
        StringBuilder result = new StringBuilder();
        int i = 0;
        while (i < s.length()) {
            if (s.charAt(i) == '(') {
                int j = s.indexOf(')', i + 1);
                String key = s.substring(i + 1, j);
                result.append(lookup.getOrDefault(key, "?"));
                i = j + 1;
            } else {
                result.append(s.charAt(i));
                i++;
            }
        }
        return result.toString();
    }
}
