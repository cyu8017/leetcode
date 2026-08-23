// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

using System.Collections.Generic;

public class Solution {
    public long InterchangeableRectangles(int[][] rectangles) {
        int Gcd(int a, int b) {
            while (b != 0) { int t = a % b; a = b; b = t; }
            return a;
        }
        var freq = new Dictionary<(int, int), int>();
        long ans = 0;
        foreach (var rect in rectangles) {
            int g = Gcd(rect[0], rect[1]);
            var key = (rect[0] / g, rect[1] / g);
            if (freq.TryGetValue(key, out int f)) ans += f;
            else f = 0;
            freq[key] = f + 1;
        }
        return ans;
    }
}
