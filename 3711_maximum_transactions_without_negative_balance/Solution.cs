// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

using System.Collections.Generic;

public class Solution {
    public int MaxTransactions(int[] transactions) {
        var pq = new PriorityQueue<int, int>();
        int ans = transactions.Length;
        long s = 0;
        foreach (int x in transactions) {
            s += x;
            pq.Enqueue(x, x);
            while (s < 0) {
                int y = pq.Dequeue();
                s -= y;
                ans--;
            }
        }
        return ans;
    }
}
