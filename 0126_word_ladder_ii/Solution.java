// LeetCode 0126 - Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/

import java.util.*;

class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        Set<String> words = new HashSet<>(wordList);
        if (!words.contains(endWord)) return new ArrayList<>();

        Map<String, List<String>> parents = new HashMap<>();
        Set<String> visited = new HashSet<>();
        Queue<String> queue = new ArrayDeque<>();
        visited.add(beginWord);
        queue.offer(beginWord);
        boolean found = false;

        while (!queue.isEmpty() && !found) {
            Set<String> levelVisited = new HashSet<>();
            for (int size = queue.size(); size > 0; size--) {
                String word = queue.poll();
                char[] chars = word.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        chars[i] = c;
                        String next = new String(chars);
                        if (!words.contains(next) || visited.contains(next)) continue;
                        if (levelVisited.add(next)) queue.offer(next);
                        parents.computeIfAbsent(next, k -> new ArrayList<>()).add(word);
                        if (next.equals(endWord)) found = true;
                    }
                    chars[i] = original;
                }
            }
            visited.addAll(levelVisited);
        }

        List<List<String>> result = new ArrayList<>();
        if (found) buildPaths(endWord, beginWord, parents, new ArrayList<>(), result);
        return result;
    }

    private void buildPaths(String word, String beginWord, Map<String, List<String>> parents,
                            List<String> path, List<List<String>> result) {
        path.add(word);
        if (word.equals(beginWord)) {
            List<String> ladder = new ArrayList<>(path);
            Collections.reverse(ladder);
            result.add(ladder);
        } else {
            for (String parent : parents.getOrDefault(word, Collections.emptyList())) {
                buildPaths(parent, beginWord, parents, path, result);
            }
        }
        path.remove(path.size() - 1);
    }
}