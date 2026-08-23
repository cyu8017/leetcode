// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/

import java.util.List;

class Solution {
    public int numberOfPoints(List<List<Integer>> nums) {
        int[] cov = new int[102];
        for (List<Integer> r : nums)
            for (int x = r.get(0); x <= r.get(1); x++) cov[x] = 1;
        int ans = 0;
        for (int v : cov) ans += v;
        return ans;
    }
}
