// CONFIG class=Solution method=maxItems types=None
// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

class Solution {
    public int maxItems(int[][] items, int budget) {
        int n = items.length;
        int[] frequency = new int[n + 1];
        int minimumPrice = items[0][1];
        for (int[] item : items) {
            frequency[item[0]]++;
            minimumPrice = Math.min(minimumPrice, item[1]);
        }
        List<int[]> batches = new ArrayList<>();
        for (int[] item : items) {
            int gain = 0;
            for (int multiple = item[0]; multiple <= n; multiple += item[0]) gain += frequency[multiple];
            gain--;
            if (gain > 0 && item[1] < 2 * minimumPrice) batches.add(new int[] { item[1], gain });
        }
        batches.sort(Comparator.comparingInt(a -> a[0]));
        long remaining = budget;
        long answer = budget / minimumPrice;
        long boosted = 0;
        for (int[] current : batches) {
            long count = current[1];
            long affordable = remaining / current[0];
            if (affordable < count) count = affordable;
            remaining -= count * current[0];
            boosted += count;
            long total = 2 * boosted + remaining / minimumPrice;
            if (total > answer) answer = total;
            if (count < current[1]) break;
        }
        return (int) answer;
    }
}
