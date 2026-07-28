// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<String> braceExpansionII(String expression) {
        int[] idx = new int[] { 0 };
        Set<String> result = parse(expression, idx);
        List<String> ans = new ArrayList<>(result);
        Collections.sort(ans);
        return ans;
    }

    private Set<String> parse(String expr, int[] idx) {
        Set<String> union = new HashSet<>();
        Set<String> cur = new HashSet<>();
        cur.add("");
        while (idx[0] < expr.length() && expr.charAt(idx[0]) != '}') {
            char c = expr.charAt(idx[0]);
            if (c == '{') {
                idx[0]++;
                Set<String> nested = parse(expr, idx);
                Set<String> next = new HashSet<>();
                for (String a : cur) {
                    for (String b : nested) {
                        next.add(a + b);
                    }
                }
                cur = next;
            } else if (c == ',') {
                union.addAll(cur);
                cur = new HashSet<>();
                cur.add("");
                idx[0]++;
            } else {
                int j = idx[0];
                while (j < expr.length() && Character.isLowerCase(expr.charAt(j))) {
                    j++;
                }
                String token = expr.substring(idx[0], j);
                Set<String> next = new HashSet<>();
                for (String a : cur) {
                    next.add(a + token);
                }
                cur = next;
                idx[0] = j;
            }
        }
        union.addAll(cur);
        idx[0]++; // skip '}'
        return union;
    }
}
