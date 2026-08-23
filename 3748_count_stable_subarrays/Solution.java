// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count_stable_subarrays/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public long[] countStableSubarrays(int[] nums, int[][] queries) {
        int n = nums.length;
        List<Integer> seg = new ArrayList<>();
        List<Long> s = new ArrayList<>();
        s.add(0L);
        int l = 0;
        for (int r = 0; r < n; r++) {
            if (r == n - 1 || nums[r] > nums[r + 1]) {
                seg.add(l);
                long k = r - l + 1;
                s.add(s.get(s.size() - 1) + k * (k + 1) / 2);
                l = r + 1;
            }
        }
        long[] ans = new long[queries.length];
        for (int idx = 0; idx < queries.length; idx++) {
            int left = queries[idx][0], right = queries[idx][1];
            int i = lowerBound(seg, left + 1);
            int j = lowerBound(seg, right + 1) - 1;
            if (i > j) {
                long k = right - left + 1;
                ans[idx] = k * (k + 1) / 2;
            } else {
                long a = seg.get(i) - left;
                long b = right - seg.get(j) + 1;
                ans[idx] = a * (a + 1) / 2 + s.get(j) - s.get(i) + b * (b + 1) / 2;
            }
        }
        return ans;
    }

    private int lowerBound(List<Integer> a, int x) {
        int lo = 0, hi = a.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a.get(mid) < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
