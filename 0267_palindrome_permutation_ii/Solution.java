// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<String> generatePalindromes(String s) {
        Map<Character, Integer> counts = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            counts.put(ch, counts.getOrDefault(ch, 0) + 1);
        }

        String middle = "";
        List<Character> oddChars = new ArrayList<>();
        for (Map.Entry<Character, Integer> entry : counts.entrySet()) {
            if (entry.getValue() % 2 != 0) {
                oddChars.add(entry.getKey());
            }
        }
        if (oddChars.size() > 1) {
            return new ArrayList<>();
        }
        if (oddChars.size() == 1) {
            middle = String.valueOf(oddChars.get(0));
        }

        char[] keys = new char[counts.size()];
        int keyIndex = 0;
        for (char ch : counts.keySet()) {
            keys[keyIndex++] = ch;
        }
        Arrays.sort(keys);

        char[] half = new char[s.length() / 2];
        int halfIndex = 0;
        for (char ch : keys) {
            int count = counts.get(ch) / 2;
            for (int i = 0; i < count; i++) {
                half[halfIndex++] = ch;
            }
        }

        List<String> result = new ArrayList<>();
        boolean[] used = new boolean[half.length];
        char[] path = new char[half.length];
        backtrack(half, used, path, 0, middle, result);
        return result;
    }

    private void backtrack(
            char[] half,
            boolean[] used,
            char[] path,
            int depth,
            String middle,
            List<String> result) {
        if (depth == half.length) {
            String prefix = new String(path);
            result.add(prefix + middle + new StringBuilder(prefix).reverse());
            return;
        }
        for (int index = 0; index < half.length; index++) {
            if (used[index]) {
                continue;
            }
            if (index > 0 && half[index] == half[index - 1] && !used[index - 1]) {
                continue;
            }
            used[index] = true;
            path[depth] = half[index];
            backtrack(half, used, path, depth + 1, middle, result);
            used[index] = false;
        }
    }
}
