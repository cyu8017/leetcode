// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

using System.Collections.Generic;

public class Solution {
    class BIT {
        int n;
        int[] c;
        public BIT(int n_) { n = n_; c = new int[n_ + 1]; }
        public void Update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        public int Query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    }

    public int[] MinDeletions(string s, int[][] queries) {
        int n = s.Length;
        int[] nums = new int[n];
        var bit = new BIT(n);
        for (int i = 1; i < n; i++) {
            if (s[i] == s[i - 1]) {
                nums[i] = 1;
                bit.Update(i + 1, 1);
            }
        }
        var ans = new List<int>();
        foreach (var q in queries) {
            if (q[0] == 1) {
                int j = q[1];
                int delta = (nums[j] ^ 1) - nums[j];
                nums[j] ^= 1;
                bit.Update(j + 1, delta);
                if (j + 1 < n) {
                    delta = (nums[j + 1] ^ 1) - nums[j + 1];
                    nums[j + 1] ^= 1;
                    bit.Update(j + 2, delta);
                }
            } else {
                int l = q[1], r = q[2];
                ans.Add(bit.Query(r + 1) - bit.Query(l + 1));
            }
        }
        return ans.ToArray();
    }
}
