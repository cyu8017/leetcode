// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    public long[] findMaxSum(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        int[][] arr = new int[n][3];
        for (int i = 0; i < n; i++) {
            arr[i][0] = nums1[i];
            arr[i][1] = nums2[i];
            arr[i][2] = i;
        }
        Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));
        long[] ans = new long[n];
        PriorityQueue<Integer> h = new PriorityQueue<>();
        long sum = 0;
        for (int i = 0; i < n; ) {
            int v = arr[i][0];
            int start = i;
            while (i < n && arr[i][0] == v) i++;
            for (int t = start; t < i; t++) ans[arr[t][2]] = sum;
            for (int t = start; t < i; t++) {
                h.offer(arr[t][1]);
                sum += arr[t][1];
                if (h.size() > k) sum -= h.poll();
            }
        }
        return ans;
    }
}
