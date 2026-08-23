// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

class Solution {
    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> graph = new HashMap<>();
        Map<Character, Integer> indegree = new HashMap<>();

        for (String word : words) {
            for (int i = 0; i < word.length(); i++) {
                char ch = word.charAt(i);
                graph.putIfAbsent(ch, new HashSet<>());
                indegree.putIfAbsent(ch, 0);
            }
        }

        for (int i = 0; i < words.length - 1; i++) {
            String first = words[i];
            String second = words[i + 1];
            if (first.length() > second.length() && first.startsWith(second)) {
                return "";
            }
            int limit = Math.min(first.length(), second.length());
            for (int j = 0; j < limit; j++) {
                char left = first.charAt(j);
                char right = second.charAt(j);
                if (left != right) {
                    if (!graph.get(left).contains(right)) {
                        graph.get(left).add(right);
                        indegree.put(right, indegree.get(right) + 1);
                    }
                    break;
                }
            }
        }

        Queue<Character> queue = new ArrayDeque<>();
        for (Map.Entry<Character, Integer> entry : indegree.entrySet()) {
            if (entry.getValue() == 0) {
                queue.offer(entry.getKey());
            }
        }

        StringBuilder order = new StringBuilder();
        while (!queue.isEmpty()) {
            char ch = queue.poll();
            order.append(ch);
            for (char next : graph.get(ch)) {
                indegree.put(next, indegree.get(next) - 1);
                if (indegree.get(next) == 0) {
                    queue.offer(next);
                }
            }
        }

        return order.length() == indegree.size() ? order.toString() : "";
    }
}
