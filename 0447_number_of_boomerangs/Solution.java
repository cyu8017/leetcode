// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int total = 0;
        for (int[] anchor : points) {
            Map<Long, Integer> distances = new HashMap<>();
            for (int[] other : points) {
                int dx = anchor[0] - other[0];
                int dy = anchor[1] - other[1];
                long distance = (long) dx * dx + (long) dy * dy;
                distances.merge(distance, 1, Integer::sum);
            }
            for (int count : distances.values()) {
                total += count * (count - 1);
            }
        }
        return total;
    }
}
