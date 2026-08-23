// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static class BIT {
        int n;
        int[] c;

        BIT(int n) {
            this.n = n;
            c = new int[n + 1];
        }

        void update(int x, int delta) {
            for (; x <= n; x += x & -x) {
                c[x] += delta;
            }
        }

        int query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) {
                s += c[x];
            }
            return s;
        }
    }

    public int[] countOfPeaks(int[] nums, int[][] queries) {
        int n = nums.length;
        BIT tree = new BIT(n - 1);
        for (int i = 1; i < n - 1; i++) {
            updatePeak(nums, tree, n, i, 1);
        }
        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            if (q[0] == 1) {
                int l = q[1] + 1, r = q[2] - 1, t = 0;
                if (l <= r) {
                    t = tree.query(r) - tree.query(l - 1);
                }
                ans.add(t);
            } else {
                int idx = q[1], val = q[2];
                for (int i = idx - 1; i <= idx + 1; i++) {
                    updatePeak(nums, tree, n, i, -1);
                }
                nums[idx] = val;
                for (int i = idx - 1; i <= idx + 1; i++) {
                    updatePeak(nums, tree, n, i, 1);
                }
            }
        }
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            res[i] = ans.get(i);
        }
        return res;
    }

    private void updatePeak(int[] nums, BIT tree, int n, int i, int val) {
        if (i <= 0 || i >= n - 1) {
            return;
        }
        if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1]) {
            tree.update(i, val);
        }
    }
}
