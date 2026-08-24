// LeetCode 2251 - Number of Flowers in Full Bloom
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] fullBloomFlowers(int[][] flowers, int[] people) {
        List<Integer> start = new ArrayList<>();
        List<Integer> end = new ArrayList<>();
        for (int[] f : flowers) {
            start.add(f[0]);
            end.add(f[1]);
        }
        Collections.sort(start);
        Collections.sort(end);
        int[] ans = new int[people.length];
        for (int i = 0; i < people.length; i++) {
            int t = people[i];
            ans[i] = upperBound(start, t) - lowerBound(end, t);
        }
        return ans;
    }

    private int upperBound(List<Integer> a, int t) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) <= t) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    private int lowerBound(List<Integer> a, int t) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) < t) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
