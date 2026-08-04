// LeetCode 1345 - Jump Game Iv
// https://leetcode.com/problems/jump-game-iv/

import java.util.*;

class Solution {
    public int minJumps(int[] arr) {
        Map<Integer, List<Integer>> positions = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            positions.computeIfAbsent(arr[i], k -> new ArrayList<>()).add(i);
        }
        Queue<Integer> queue = new ArrayDeque<>();
        boolean[] seen = new boolean[arr.length];
        queue.offer(0);
        seen[0] = true;
        int steps = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int s = 0; s < size; s++) {
                int i = queue.poll();
                if (i == arr.length - 1) return steps;
                List<Integer> next = new ArrayList<>(positions.getOrDefault(arr[i], List.of()));
                positions.remove(arr[i]);
                next.add(i - 1);
                next.add(i + 1);
                for (int j : next) {
                    if (j >= 0 && j < arr.length && !seen[j]) {
                        seen[j] = true;
                        queue.offer(j);
                    }
                }
            }
            steps++;
        }
        return -1;
    }
}
