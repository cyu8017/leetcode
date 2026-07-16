// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<List<String>> wordSquares(String[] words) {
        Arrays.sort(words);
        int length = words[0].length();
        Map<String, List<String>> prefixMap = new HashMap<>();
        prefixMap.put("", new ArrayList<>(Arrays.asList(words)));

        for (String word : words) {
            for (int index = 0; index < word.length(); index++) {
                String prefix = word.substring(0, index + 1);
                prefixMap.computeIfAbsent(prefix, key -> new ArrayList<>()).add(word);
            }
        }

        List<List<String>> squares = new ArrayList<>();
        List<String> current = new ArrayList<>();
        dfs(0, length, current, prefixMap, squares);
        return squares;
    }

    private void dfs(
            int row,
            int length,
            List<String> current,
            Map<String, List<String>> prefixMap,
            List<List<String>> squares) {
        if (row == length) {
            squares.add(new ArrayList<>(current));
            return;
        }

        StringBuilder prefixBuilder = new StringBuilder();
        for (String word : current) {
            prefixBuilder.append(word.charAt(row));
        }
        String prefix = prefixBuilder.toString();

        for (String candidate : prefixMap.getOrDefault(prefix, List.of())) {
            current.add(candidate);
            dfs(row + 1, length, current, prefixMap, squares);
            current.remove(current.size() - 1);
        }
    }
}
