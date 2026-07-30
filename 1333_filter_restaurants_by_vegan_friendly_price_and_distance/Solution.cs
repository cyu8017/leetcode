// LeetCode 1333 - Filter Restaurants By Vegan Friendly Price And Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

using System.Collections.Generic;

public class Solution {
    public int[] FilterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        var valid = new List<int[]>();
        foreach (var row in restaurants)
            if ((veganFriendly == 0 || row[2] == 1) && row[3] <= maxPrice && row[4] <= maxDistance)
                valid.Add(row);
        valid.Sort((a, b) => {
            int cmp = b[1].CompareTo(a[1]);
            return cmp != 0 ? cmp : b[0].CompareTo(a[0]);
        });
        var answer = new int[valid.Count];
        for (int i = 0; i < valid.Count; i++) answer[i] = valid[i][0];
        return answer;
    }
}
