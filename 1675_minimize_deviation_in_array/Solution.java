// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

import java.util.PriorityQueue;

class Solution {
    public int minimumDeviation(int[] nums) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        int min = Integer.MAX_VALUE;
        for (int x : nums) {
            if ((x & 1) == 1) {
                x *= 2;
            }
            maxHeap.offer(x);
            min = Math.min(min, x);
        }
        int ans = Integer.MAX_VALUE;
        while (true) {
            int x = maxHeap.poll();
            ans = Math.min(ans, x - min);
            if ((x & 1) == 1) {
                return ans;
            }
            x /= 2;
            min = Math.min(min, x);
            maxHeap.offer(x);
        }
    }
}
