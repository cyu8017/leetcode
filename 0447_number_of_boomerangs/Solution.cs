// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

using System.Collections.Generic;

public class Solution {
    public int NumberOfBoomerangs(int[][] points) {
        int total = 0;
        foreach (int[] anchor in points) {
            Dictionary<long, int> distances = new Dictionary<long, int>();
            foreach (int[] other in points) {
                int dx = anchor[0] - other[0];
                int dy = anchor[1] - other[1];
                long distance = (long)dx * dx + (long)dy * dy;
                distances[distance] = distances.GetValueOrDefault(distance, 0) + 1;
            }
            foreach (int count in distances.Values) {
                total += count * (count - 1);
            }
        }
        return total;
    }
}
