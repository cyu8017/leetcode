// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] countRectangles(int[][] rectangles, int[][] points) {
        @SuppressWarnings("unchecked")
        List<Integer>[] byH = new ArrayList[101];
        for (int h = 0; h <= 100; h++) byH[h] = new ArrayList<>();
        for (int[] r : rectangles) byH[r[1]].add(r[0]);
        for (int h = 1; h <= 100; h++) Collections.sort(byH[h]);
        int[] ans = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            int x = points[i][0], y = points[i][1], cnt = 0;
            for (int h = y; h <= 100; h++) {
                List<Integer> xs = byH[h];
                int lo = 0, hi = xs.size();
                while (lo < hi) {
                    int mid = (lo + hi) / 2;
                    if (xs.get(mid) < x) lo = mid + 1;
                    else hi = mid;
                }
                cnt += xs.size() - lo;
            }
            ans[i] = cnt;
        }
        return ans;
    }
}
