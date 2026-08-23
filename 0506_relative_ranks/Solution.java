// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String[] findRelativeRanks(int[] score) {
        Map<Integer, String> medals = new HashMap<>();
        medals.put(1, "Gold Medal");
        medals.put(2, "Silver Medal");
        medals.put(3, "Bronze Medal");
        Integer[] order = new Integer[score.length];
        for (int index = 0; index < score.length; index++) {
            order[index] = index;
        }
        java.util.Arrays.sort(order, (left, right) -> Integer.compare(score[right], score[left]));
        String[] result = new String[score.length];
        for (int rank = 0; rank < order.length; rank++) {
            int index = order[rank];
            result[index] = medals.getOrDefault(rank + 1, String.valueOf(rank + 1));
        }
        return result;
    }
}
