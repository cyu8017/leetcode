// LeetCode 1307 - Verbal Arithmetic Puzzle
// https://leetcode.com/problems/verbal-arithmetic-puzzle/

import java.util.*;

class Solution {
    private String[] words;
    private String result;
    private Map<Character, Integer> value = new HashMap<>();
    private boolean[] used = new boolean[10];
    private Set<Character> leading = new HashSet<>();
    private int width;

    public boolean isSolvable(String[] words, String result) {
        this.words = words;
        this.result = result;
        int maxWord = 0;
        Set<Character> letters = new HashSet<>();
        for (String w : words) {
            maxWord = Math.max(maxWord, w.length());
            for (char c : w.toCharArray()) letters.add(c);
            if (w.length() > 1) leading.add(w.charAt(0));
        }
        for (char c : result.toCharArray()) letters.add(c);
        if (result.length() > 1) leading.add(result.charAt(0));
        if (maxWord > result.length() || letters.size() > 10) return false;
        width = result.length();
        return solve(0, 0, 0);
    }

    private boolean solve(int column, int row, int total) {
        if (column == width) return total == 0;
        if (row < words.length) {
            if (column >= words[row].length()) return solve(column, row + 1, total);
            char ch = words[row].charAt(words[row].length() - 1 - column);
            if (value.containsKey(ch)) return solve(column, row + 1, total + value.get(ch));
            for (int digit = 0; digit < 10; digit++) {
                if (!used[digit] && (digit != 0 || !leading.contains(ch))) {
                    value.put(ch, digit);
                    used[digit] = true;
                    if (solve(column, row + 1, total + digit)) return true;
                    used[digit] = false;
                    value.remove(ch);
                }
            }
            return false;
        }
        char ch = result.charAt(result.length() - 1 - column);
        int digit = total % 10, carry = total / 10;
        if (value.containsKey(ch)) {
            return value.get(ch) == digit && solve(column + 1, 0, carry);
        }
        if (used[digit] || (digit == 0 && leading.contains(ch))) return false;
        value.put(ch, digit);
        used[digit] = true;
        boolean ok = solve(column + 1, 0, carry);
        used[digit] = false;
        value.remove(ch);
        return ok;
    }
}
