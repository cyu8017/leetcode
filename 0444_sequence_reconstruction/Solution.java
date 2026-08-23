// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public boolean sequenceReconstruction(int[] nums, int[][] sequences) {
        Map<Integer, Integer> indegree = new HashMap<>();
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        for (int value : nums) {
            indegree.put(value, 0);
            graph.put(value, new HashSet<>());
        }

        Set<String> seenEdges = new HashSet<>();
        for (int[] sequence : sequences) {
            for (int index = 0; index < sequence.length - 1; index++) {
                int left = sequence[index];
                int right = sequence[index + 1];
                String edge = left + "," + right;
                if (seenEdges.contains(edge)) {
                    continue;
                }
                seenEdges.add(edge);
                graph.get(left).add(right);
                indegree.put(right, indegree.get(right) + 1);
            }
        }

        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int value : nums) {
            if (indegree.get(value) == 0) {
                queue.add(value);
            }
        }

        List<Integer> order = new ArrayList<>();
        while (!queue.isEmpty()) {
            if (queue.size() > 1) {
                return false;
            }
            int node = queue.removeFirst();
            order.add(node);
            for (int neighbor : graph.get(node)) {
                indegree.put(neighbor, indegree.get(neighbor) - 1);
                if (indegree.get(neighbor) == 0) {
                    queue.add(neighbor);
                }
            }
        }

        if (order.size() != nums.length) {
            return false;
        }
        for (int index = 0; index < nums.length; index++) {
            if (order.get(index) != nums[index]) {
                return false;
            }
        }
        return true;
    }
}
