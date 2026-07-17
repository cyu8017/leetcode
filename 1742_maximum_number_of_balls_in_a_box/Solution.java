// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int value = lowLimit; value <= highLimit; value++) {
            int box = 0;
            int v = value;
            while (v > 0) {
                box += v % 10;
                v /= 10;
            }
            counts.merge(box, 1, Integer::sum);
        }
        int max = 0;
        for (int count : counts.values()) {
            max = Math.max(max, count);
        }
        return max;
    }
}
