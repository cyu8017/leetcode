// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

import java.util.*;

class Solution {
    public List<String> ambiguousCoordinates(String s) {
        String digits = s.substring(1, s.length() - 1);
        List<String> answer = new ArrayList<>();
        for (int i = 1; i < digits.length(); i++) {
            for (String left : candidates(digits.substring(0, i))) {
                for (String right : candidates(digits.substring(i))) {
                    answer.add("(" + left + ", " + right + ")");
                }
            }
        }
        return answer;
    }

    private List<String> candidates(String frag) {
        List<String> options = new ArrayList<>();
        if (frag.isEmpty() || (frag.length() > 1 && frag.charAt(0) == '0' && frag.charAt(frag.length() - 1) == '0')) {
            return options;
        }
        if (frag.charAt(0) == '0' && frag.length() > 1) {
            if (frag.charAt(frag.length() - 1) != '0') options.add("0." + frag.substring(1));
            return options;
        }
        options.add(frag);
        if (frag.charAt(frag.length() - 1) == '0') return options;
        for (int i = 1; i < frag.length(); i++) {
            options.add(frag.substring(0, i) + "." + frag.substring(i));
        }
        return options;
    }
}
