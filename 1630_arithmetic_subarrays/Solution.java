// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

import java.util.*;

class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        List<Boolean> ans = new ArrayList<>();
        for (int t = 0; t < l.length; t++) {
            int a = l[t], b = r[t];
            int[] x = Arrays.copyOfRange(nums, a, b + 1);
            Arrays.sort(x);
            boolean ok = true;
            if (x.length >= 3) {
                int diff = x[1] - x[0];
                for (int i = 2; i < x.length; i++) {
                    if (x[i] - x[i - 1] != diff) { ok = false; break; }
                }
            }
            ans.add(ok);
        }
        return ans;
    }
}
