// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

using System.Collections.Generic;

public class Solution {
    class BIT {
        int n;
        int[] c;
        public BIT(int n) { this.n = n; c = new int[n + 1]; }
        public void Update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        public int Query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    }

    public int[] CountOfPeaks(int[] nums, int[][] queries) {
        int n = nums.Length;
        var tree = new BIT(n - 1);
        void Update(int i, int val) {
            if (i <= 0 || i >= n - 1) return;
            if (nums[i - 1] < nums[i] && nums[i] > nums[i + 1]) tree.Update(i, val);
        }
        for (int i = 1; i < n - 1; i++) Update(i, 1);
        var ans = new List<int>();
        foreach (var q in queries) {
            if (q[0] == 1) {
                int l = q[1] + 1, r = q[2] - 1, t = 0;
                if (l <= r) t = tree.Query(r) - tree.Query(l - 1);
                ans.Add(t);
            } else {
                int idx = q[1], val = q[2];
                for (int i = idx - 1; i <= idx + 1; i++) Update(i, -1);
                nums[idx] = val;
                for (int i = idx - 1; i <= idx + 1; i++) Update(i, 1);
            }
        }
        return ans.ToArray();
    }
}
