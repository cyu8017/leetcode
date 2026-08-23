// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

import java.util.*;

class Solution {
    public String countOfAtoms(String formula) {
        Deque<TreeMap<String, Integer>> st = new ArrayDeque<>();
        st.push(new TreeMap<>());
        int i = 0, n = formula.length();
        while (i < n) {
            if (formula.charAt(i) == '(') {
                st.push(new TreeMap<>());
                i++;
            } else if (formula.charAt(i) == ')') {
                i++;
                int start = i;
                while (i < n && Character.isDigit(formula.charAt(i))) i++;
                int mult = start < i ? Integer.parseInt(formula.substring(start, i)) : 1;
                TreeMap<String, Integer> top = st.pop();
                for (Map.Entry<String, Integer> kv : top.entrySet()) {
                    st.peek().put(kv.getKey(), st.peek().getOrDefault(kv.getKey(), 0) + kv.getValue() * mult);
                }
            } else {
                int start = i++;
                while (i < n && Character.isLowerCase(formula.charAt(i))) i++;
                String atom = formula.substring(start, i);
                start = i;
                while (i < n && Character.isDigit(formula.charAt(i))) i++;
                int count = start < i ? Integer.parseInt(formula.substring(start, i)) : 1;
                st.peek().put(atom, st.peek().getOrDefault(atom, 0) + count);
            }
        }
        StringBuilder result = new StringBuilder();
        for (Map.Entry<String, Integer> kv : st.peek().entrySet()) {
            result.append(kv.getKey());
            if (kv.getValue() > 1) result.append(kv.getValue());
        }
        return result.toString();
    }
}
