// LeetCode 1383 - Maximum Performance Of A Team
// https://leetcode.com/problems/maximum-performance-of-a-team/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int MaxPerformance(int n, int[] speed, int[] efficiency, int k) {
        var order = Enumerable.Range(0, n).OrderByDescending(i => efficiency[i]).ToArray();
        var h = new PriorityQueue<int, int>();
        long total = 0, ans = 0;
        foreach (int i in order) {
            h.Enqueue(speed[i], speed[i]); total += speed[i];
            if (h.Count > k) total -= h.Dequeue();
            ans = System.Math.Max(ans, total * efficiency[i]);
        }
        return (int)(ans % 1000000007);
    }
}
