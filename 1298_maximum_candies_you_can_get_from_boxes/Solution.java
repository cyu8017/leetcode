// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

import java.util.*;

class Solution {
    public int maxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        HashSet<Integer> owned = new HashSet<>();
        for (int box : initialBoxes) owned.add(box);
        HashSet<Integer> opened = new HashSet<>();
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int box : initialBoxes) {
            if (status[box] == 1) queue.add(box);
        }
        int total = 0;
        while (!queue.isEmpty()) {
            int box = queue.poll();
            if (opened.contains(box) || status[box] == 0) continue;
            opened.add(box);
            total += candies[box];
            for (int key : keys[box]) {
                status[key] = 1;
                if (owned.contains(key) && !opened.contains(key)) queue.add(key);
            }
            for (int child : containedBoxes[box]) {
                owned.add(child);
                if (status[child] == 1 && !opened.contains(child)) queue.add(child);
            }
        }
        return total;
    }
}
