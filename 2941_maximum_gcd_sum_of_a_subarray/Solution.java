// LeetCode 2941 - Maximum GCD-Sum of a Subarray
// https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

import java.util.ArrayList;
import java.util.List;

class Solution {
    static int gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }

    public long maxGcdSum(int[] nums, int k) {
        int n = nums.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        long ans = 0;
        List<int[]> st = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            List<int[]> nst = new ArrayList<>();
            nst.add(new int[]{nums[i], i});
            for (int[] p : st) {
                int g = gcd(p[0], nums[i]);
                if (nst.get(nst.size() - 1)[0] == g) continue;
                nst.add(new int[]{g, p[1]});
            }
            st = nst;
            for (int[] p : st) {
                int g = p[0], idx = p[1];
                if (i - idx + 1 >= k) {
                    long cand = (pref[i + 1] - pref[idx]) * g;
                    if (cand > ans) ans = cand;
                }
            }
        }
        return ans;
    }
}
