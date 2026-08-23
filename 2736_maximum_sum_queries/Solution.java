// LeetCode 2736 - Maximum Sum Queries
// https://leetcode.com/problems/maximum-sum-queries/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] maximumSumQueries(int[] nums1, int[] nums2, int[][] queries) {
        int n = nums1.length;
        int[][] pts = new int[n][3];
        for (int i = 0; i < n; i++) {
            pts[i][0] = nums1[i];
            pts[i][1] = nums2[i];
            pts[i][2] = nums1[i] + nums2[i];
        }
        Arrays.sort(pts, (a, b) -> Integer.compare(b[0], a[0]));
        int[][] qs = new int[queries.length][3];
        for (int i = 0; i < queries.length; i++) {
            qs[i][0] = queries[i][0];
            qs[i][1] = queries[i][1];
            qs[i][2] = i;
        }
        Arrays.sort(qs, (a, b) -> Integer.compare(b[0], a[0]));
        List<Integer> ys = new ArrayList<>();
        for (int y : nums2) ys.add(y);
        for (int[] q : queries) ys.add(q[1]);
        Collections.sort(ys);
        int w = 0;
        for (int i = 0; i < ys.size(); i++) {
            if (i == 0 || !ys.get(i).equals(ys.get(i - 1))) ys.set(w++, ys.get(i));
        }
        ys = ys.subList(0, w);
        int m = ys.size();
        int[] bit = new int[m + 2];
        Arrays.fill(bit, -1);
        int[] ans = new int[queries.length];
        int j = 0;
        for (int[] q : qs) {
            while (j < n && pts[j][0] >= q[0]) {
                update(bit, m, m - rank(ys, pts[j][1]) + 1, pts[j][2]);
                j++;
            }
            ans[q[2]] = query(bit, m - rank(ys, q[1]) + 1);
        }
        return ans;
    }

    private int rank(List<Integer> ys, int y) {
        int lo = 0, hi = ys.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (ys.get(mid) < y) lo = mid + 1;
            else hi = mid;
        }
        return lo + 1;
    }

    private void update(int[] bit, int m, int i, int v) {
        for (; i <= m; i += i & -i) bit[i] = Math.max(bit[i], v);
    }

    private int query(int[] bit, int i) {
        int best = -1;
        for (; i > 0; i -= i & -i) best = Math.max(best, bit[i]);
        return best;
    }
}
