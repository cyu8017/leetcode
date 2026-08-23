// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public long kSum(int[] nums, int k) {
        long total = 0;
        int n = nums.length;
        int[] absNums = new int[n];
        for (int i = 0; i < n; i++) {
            if (nums[i] >= 0) {
                total += nums[i];
                absNums[i] = nums[i];
            } else {
                absNums[i] = -nums[i];
            }
        }
        Arrays.sort(absNums);
        PriorityQueue<long[]> h = new PriorityQueue<>((a, b) -> Long.compare(b[0], a[0]));
        h.offer(new long[] {total, 0});
        for (int t = 0; t < k - 1; t++) {
            long[] cur = h.poll();
            long sum = cur[0];
            int i = (int) cur[1];
            if (i >= absNums.length) continue;
            h.offer(new long[] {sum - absNums[i], i + 1});
            if (i > 0) {
                h.offer(new long[] {sum - absNums[i] + absNums[i - 1], i + 1});
            }
        }
        return h.peek()[0];
    }
}
