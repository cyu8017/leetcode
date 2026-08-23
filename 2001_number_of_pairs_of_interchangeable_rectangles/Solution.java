// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

import java.util.*;

class Solution {
    public long interchangeableRectangles(int[][] rectangles) {
        Map<String, Integer> freq = new HashMap<>();
        long ans = 0;
        for (int[] rect : rectangles) {
            int g = gcd(rect[0], rect[1]);
            String key = (rect[0] / g) + "/" + (rect[1] / g);
            int f = freq.getOrDefault(key, 0);
            ans += f;
            freq.put(key, f + 1);
        }
        return ans;
    }

    private int gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }
}
