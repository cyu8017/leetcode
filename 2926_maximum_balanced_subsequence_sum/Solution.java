// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    private long[] bit;
    private static final long NEG_INF = -(1L << 60);

    public long maxBalancedSubsequenceSum(int[] nums) {
        int n = nums.length;
        int[] keys = new int[n];
        List<Integer> uniq = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            keys[i] = nums[i] - i;
            uniq.add(keys[i]);
        }
        Collections.sort(uniq);
        List<Integer> compact = new ArrayList<>();
        for (int v : uniq) {
            if (compact.isEmpty() || compact.get(compact.size() - 1) != v) compact.add(v);
        }
        uniq = compact;
        bit = new long[uniq.size() + 2];
        for (int i = 0; i < bit.length; i++) bit[i] = NEG_INF;
        long ans = NEG_INF;
        for (int i = 0; i < n; i++) {
            int id = idxOf(uniq, keys[i]);
            long best = query(id);
            long cur = nums[i];
            if (best > NEG_INF / 2) {
                long cand = best + nums[i];
                if (cand > cur) cur = cand;
            }
            update(id, cur);
            if (cur > ans) ans = cur;
        }
        return ans;
    }

    private int idxOf(List<Integer> uniq, int v) {
        int lo = 0, hi = uniq.size();
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (uniq.get(mid) < v) lo = mid + 1;
            else hi = mid;
        }
        return lo + 1;
    }

    private void update(int i, long val) {
        for (; i < bit.length; i += i & -i)
            if (val > bit[i]) bit[i] = val;
    }

    private long query(int i) {
        long best = NEG_INF;
        for (; i > 0; i -= i & -i)
            if (bit[i] > best) best = bit[i];
        return best;
    }
}
