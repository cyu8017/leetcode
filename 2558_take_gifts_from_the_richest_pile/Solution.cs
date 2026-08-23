// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

using System;
using System.Collections.Generic;

public class Solution {
    public long PickGifts(int[] gifts, int k) {
        var h = new PriorityQueue<int, int>();
        foreach (int g in gifts) h.Enqueue(g, -g);
        for (int i = 0; i < k; ++i) {
            int x = h.Dequeue();
            int y = (int)Math.Sqrt(x);
            h.Enqueue(y, -y);
        }
        long ans = 0;
        while (h.Count > 0) ans += h.Dequeue();
        return ans;
    }
}
