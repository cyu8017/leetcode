// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

using System;

public class Solution {
    public int MaxIceCream(int[] costs, int coins) {
        Array.Sort(costs);
        int count = 0;
        foreach (int cost in costs) {
            if (coins < cost) break;
            coins -= cost;
            count++;
        }
        return count;
    }
}
