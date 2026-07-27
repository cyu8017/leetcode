// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

import java.util.Arrays;

class Solution {
    public int minimumEffort(int[][] tasks) {
        Arrays.sort(tasks, (a, b) -> Integer.compare(b[1] - b[0], a[1] - a[0]));
        int energy = 0;
        int spent = 0;
        for (int[] task : tasks) {
            energy = Math.max(energy, spent + task[1]);
            spent += task[0];
        }
        return energy;
    }
}
