// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

import java.util.*;

class Solution {
    private final Map<String, List<Character>> transitions = new HashMap<>();
    private final Map<String, Boolean> memo = new HashMap<>();

    public boolean pyramidTransition(String bottom, List<String> allowed) {
        transitions.clear();
        memo.clear();
        for (String triple : allowed) {
            String key = triple.substring(0, 2);
            transitions.computeIfAbsent(key, x -> new ArrayList<>()).add(triple.charAt(2));
        }
        return dfs(bottom);
    }

    private boolean dfs(String row) {
        if (row.length() == 1) return true;
        if (memo.containsKey(row)) return memo.get(row);
        List<List<Character>> options = new ArrayList<>();
        for (int i = 0; i + 1 < row.length(); i++) {
            String key = row.substring(i, i + 2);
            if (!transitions.containsKey(key)) {
                memo.put(row, false);
                return false;
            }
            options.add(transitions.get(key));
        }
        StringBuilder path = new StringBuilder();
        boolean ok = build(0, options, path);
        memo.put(row, ok);
        return ok;
    }

    private boolean build(int index, List<List<Character>> options, StringBuilder path) {
        if (index == options.size()) return dfs(path.toString());
        for (char ch : options.get(index)) {
            path.append(ch);
            if (build(index + 1, options, path)) return true;
            path.setLength(path.length() - 1);
        }
        return false;
    }
}
