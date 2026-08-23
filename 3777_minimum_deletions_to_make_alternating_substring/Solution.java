// LeetCode 3777 - Minimum Deletions To Make Alternating Substring
// https://leetcode.com/problems/minimum-deletions-to-make-alternating-substring/

import java.util.ArrayList;
import java.util.List;

class Solution {
    class BIT {
        int n;
        int[] c;
        public BIT(int n_) { n = n_; c = new int[n_ + 1]; }
        public void update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        public int query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    }

    public int[] minDeletions(String s, int[][] queries) {
        int n = s.length();
        int[] nums = new int[n];
        var bit = new BIT(n);
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                nums[i] = 1;
                bit.update(i + 1, 1);
            }
        }
        var ans = new ArrayList<Integer>();
        for (var q : queries) {
            if (q[0] == 1) {
                int j = q[1];
                int delta = (nums[j] ^ 1) - nums[j];
                nums[j] ^= 1;
                bit.update(j + 1, delta);
                if (j + 1 < n) {
                    delta = (nums[j + 1] ^ 1) - nums[j + 1];
                    nums[j + 1] ^= 1;
                    bit.update(j + 2, delta);
                }
            } else {
                int l = q[1], r = q[2];
                ans.add(bit.query(r + 1) - bit.query(l + 1));
            }
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
