// LeetCode 1687 - Delivering Boxes from Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int boxDelivering(int[][] boxes, int portsCount, int maxBoxes, int maxWeight) {
        int n = boxes.length;
        long[] w = new long[n + 1];
        int[] changes = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            w[i] = w[i - 1] + boxes[i - 1][1];
            changes[i] = changes[i - 1];
            if (i > 1 && boxes[i - 1][0] != boxes[i - 2][0]) {
                changes[i]++;
            }
        }
        int[] dp = new int[n + 1];
        Deque<Integer> q = new ArrayDeque<>();
        q.addLast(0);
        for (int i = 1; i <= n; i++) {
            while (!q.isEmpty() && (i - q.peekFirst() > maxBoxes || w[i] - w[q.peekFirst()] > maxWeight)) {
                q.removeFirst();
            }
            int j = q.peekFirst();
            dp[i] = dp[j] + changes[i] - changes[j + 1] + 2;
            if (i < n) {
                int val = dp[i] - changes[i + 1];
                while (!q.isEmpty() && dp[q.peekLast()] - changes[q.peekLast() + 1] >= val) {
                    q.removeLast();
                }
                q.addLast(i);
            }
        }
        return dp[n];
    }
}
