// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        Integer[] idx = new Integer[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Arrays.sort(idx, (a, b) -> Integer.compare(positions[a], positions[b]));
        List<int[]> stack = new ArrayList<>(); // i, h, d
        for (int i : idx) {
            int[] cur = new int[]{i, healths[i], directions.charAt(i)};
            while (!stack.isEmpty() && stack.get(stack.size() - 1)[2] == 'R' && cur[2] == 'L') {
                int[] top = stack.get(stack.size() - 1);
                if (top[1] == cur[1]) {
                    stack.remove(stack.size() - 1);
                    cur[1] = 0;
                    break;
                } else if (top[1] > cur[1]) {
                    top[1]--;
                    cur[1] = 0;
                    break;
                } else {
                    cur[1]--;
                    stack.remove(stack.size() - 1);
                }
            }
            if (cur[1] > 0) stack.add(cur);
        }
        Map<Integer, Integer> alive = new HashMap<>();
        for (int[] r : stack) alive.put(r[0], r[1]);
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) if (alive.containsKey(i)) ans.add(alive.get(i));
        return ans;
    }
}
