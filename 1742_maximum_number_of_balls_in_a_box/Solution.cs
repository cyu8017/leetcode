// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

public class Solution {
    public int CountBalls(int lowLimit, int highLimit) {
        var counts = new Dictionary<int, int>();
        for (int value = lowLimit; value <= highLimit; value++) {
            int box = 0;
            int v = value;
            while (v > 0) {
                box += v % 10;
                v /= 10;
            }
            counts[box] = counts.GetValueOrDefault(box) + 1;
        }
        int max = 0;
        foreach (int count in counts.Values) {
            max = Math.Max(max, count);
        }
        return max;
    }
}
