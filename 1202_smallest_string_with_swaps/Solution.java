// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

import java.util.*;

class Solution {
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        int n = s.length();
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (List<Integer> p : pairs) {
            int ra = find(parent, p.get(0)), rb = find(parent, p.get(1));
            parent[ra] = rb;
        }
        Map<Integer, PriorityQueue<Character>> groups = new HashMap<>();
        for (int i = 0; i < n; i++) {
            groups.computeIfAbsent(find(parent, i), k -> new PriorityQueue<>()).offer(s.charAt(i));
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) sb.append(groups.get(find(parent, i)).poll());
        return sb.toString();
    }
    private int find(int[] parent, int x) {
        while (parent[x] != x) { parent[x] = parent[parent[x]]; x = parent[x]; }
        return x;
    }
}
