// LeetCode 1333 - Filter Restaurants By Vegan Friendly Price And Distance
// https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

import java.util.*;

class Solution {
    public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        List<int[]> valid = new ArrayList<>();
        for (int[] row : restaurants) {
            if ((veganFriendly == 0 || row[2] == 1) && row[3] <= maxPrice && row[4] <= maxDistance) {
                valid.add(row);
            }
        }
        valid.sort((a, b) -> a[1] != b[1] ? Integer.compare(b[1], a[1]) : Integer.compare(b[0], a[0]));
        List<Integer> answer = new ArrayList<>();
        for (int[] row : valid) answer.add(row[0]);
        return answer;
    }
}
