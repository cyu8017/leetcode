// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long numberOfPairs(int[] nums1, int[] nums2, int k) {
        Map<Integer, Integer> cnt1 = new HashMap<>();
        for (int x : nums1) if (x % k == 0) cnt1.merge(x / k, 1, Integer::sum);
        if (cnt1.isEmpty()) return 0;
        Map<Integer, Integer> cnt2 = new HashMap<>();
        for (int x : nums2) cnt2.merge(x, 1, Integer::sum);
        int mx = 0;
        for (int x : cnt1.keySet()) mx = Math.max(mx, x);
        long ans = 0;
        for (Map.Entry<Integer, Integer> e : cnt2.entrySet()) {
            int x = e.getKey(), v = e.getValue();
            int s = 0;
            for (int y = x; y <= mx; y += x) {
                Integer c = cnt1.get(y);
                if (c != null) s += c;
            }
            ans += (long) s * v;
        }
        return ans;
    }
}
