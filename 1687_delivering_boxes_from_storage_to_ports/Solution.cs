// LeetCode 1687 - Delivering Boxes from Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

using System.Collections.Generic;

public class Solution {
    public int BoxDelivering(int[][] boxes, int portsCount, int maxBoxes, int maxWeight) {
        int n = boxes.Length;
        int[] w = new int[n + 1];
        int[] changes = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            w[i] = w[i - 1] + boxes[i - 1][1];
            changes[i] = changes[i - 1] + (i > 1 && boxes[i - 1][0] != boxes[i - 2][0] ? 1 : 0);
        }
        int[] dp = new int[n + 1];
        var q = new LinkedList<int>();
        q.AddLast(0);
        for (int i = 1; i <= n; i++) {
            while (q.Count > 0 && (i - q.First.Value > maxBoxes || w[i] - w[q.First.Value] > maxWeight))
                q.RemoveFirst();
            int j = q.First.Value;
            dp[i] = dp[j] + changes[i] - changes[j + 1] + 2;
            if (i < n) {
                int val = dp[i] - changes[i + 1];
                while (q.Count > 0 && dp[q.Last.Value] - changes[q.Last.Value + 1] >= val)
                    q.RemoveLast();
                q.AddLast(i);
            }
        }
        return dp[n];
    }
}
