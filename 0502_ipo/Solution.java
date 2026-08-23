// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int length = profits.length;
        int[][] projects = new int[length][2];
        for (int index = 0; index < length; index++) {
            projects[index] = new int[] { capital[index], profits[index] };
        }
        Arrays.sort(projects, (left, right) -> Integer.compare(left[0], right[0]));
        PriorityQueue<Integer> available = new PriorityQueue<>((left, right) -> Integer.compare(right, left));
        int projectIndex = 0;
        for (int round = 0; round < k; round++) {
            while (projectIndex < length && projects[projectIndex][0] <= w) {
                available.offer(projects[projectIndex][1]);
                projectIndex++;
            }
            if (available.isEmpty()) {
                break;
            }
            w += available.poll();
        }
        return w;
    }
}
