// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private int depth(long x) {
        if (x == 1) return 0;
        int d = 0;
        while (x > 1) {
            x = Long.bitCount(x);
            d++;
        }
        return d;
    }

    public int[] popcountDepth(long[] nums, long[][] queries) {
        long[] a = nums.clone();
        List<Integer> ans = new ArrayList<>();
        for (long[] q : queries) {
            if (q[0] == 1) {
                int l = (int) q[1], r = (int) q[2], k = (int) q[3], cnt = 0;
                for (int i = l; i <= r; i++)
                    if (depth(a[i]) == k) cnt++;
                ans.add(cnt);
            } else {
                a[(int) q[1]] = q[2];
            }
        }
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }
}
