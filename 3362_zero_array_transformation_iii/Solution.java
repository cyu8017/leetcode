// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public int maxRemoval(int[] nums, int[][] queries) {
        Arrays.sort(queries, (a, b) -> Integer.compare(a[0], b[0]));
        PriorityQueue<Integer> h = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        int n = nums.length;
        int[] diff = new int[n + 1];
        int j = 0, used = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            while (j < queries.length && queries[j][0] == i) {
                h.offer(queries[j][1]);
                j++;
            }
            while (cur < nums[i]) {
                if (h.isEmpty() || h.peek() < i) return -1;
                int r = h.poll();
                cur++;
                diff[r + 1]--;
                used++;
            }
        }
        return queries.length - used;
    }
}
