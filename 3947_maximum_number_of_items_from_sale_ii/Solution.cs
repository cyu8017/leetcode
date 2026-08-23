// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxItems(int[][] items, int budget) {
        int n = items.Length;
        int[] frequency = new int[n + 1];
        int minimumPrice = items[0][1];
        foreach (var item in items) {
            frequency[item[0]]++;
            minimumPrice = Math.Min(minimumPrice, item[1]);
        }
        var batches = new List<(int price, int count)>();
        foreach (var item in items) {
            int gain = 0;
            for (int multiple = item[0]; multiple <= n; multiple += item[0]) gain += frequency[multiple];
            gain--;
            if (gain > 0 && item[1] < 2 * minimumPrice) batches.Add((item[1], gain));
        }
        batches.Sort((a, b) => a.price.CompareTo(b.price));
        long remaining = budget;
        long answer = budget / minimumPrice;
        long boosted = 0;
        foreach (var current in batches) {
            long count = current.count;
            long affordable = remaining / current.price;
            if (affordable < count) count = affordable;
            remaining -= count * current.price;
            boosted += count;
            long total = 2 * boosted + remaining / minimumPrice;
            if (total > answer) answer = total;
            if (count < current.count) break;
        }
        return (int)answer;
    }
}
