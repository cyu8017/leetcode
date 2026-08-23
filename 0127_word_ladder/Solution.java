// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

import java.util.*;

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> words = new HashSet<>(wordList);
        if (!words.contains(endWord)) return 0;

        Queue<String> queue = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        queue.offer(beginWord);
        visited.add(beginWord);
        int steps = 1;

        while (!queue.isEmpty()) {
            for (int size = queue.size(); size > 0; size--) {
                String word = queue.poll();
                if (word.equals(endWord)) return steps;
                char[] chars = word.toCharArray();
                for (int i = 0; i < chars.length; i++) {
                    char original = chars[i];
                    for (char c = 'a'; c <= 'z'; c++) {
                        chars[i] = c;
                        String next = new String(chars);
                        if (words.contains(next) && visited.add(next)) queue.offer(next);
                    }
                    chars[i] = original;
                }
            }
            steps++;
        }
        return 0;
    }
}