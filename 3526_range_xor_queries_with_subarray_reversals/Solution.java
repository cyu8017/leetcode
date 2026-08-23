// LeetCode 3526 - Range XOR Queries with Subarray Reversals
// https://leetcode.com/problems/range-xor-queries-with-subarray-reversals/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] getResults(int[] nums, int[][] queries) {
        int[] a = nums.clone();
        var ans = new ArrayList<Integer>();
        for (var q : queries) {
            int typ = q[0];
            if (typ == 1) {
                int l = q[1], r = q[2];
                while (l < r) { int tmp = a[l]; a[l] = a[r]; a[r] = tmp; l++; r--; }
            } else if (typ == 2) {
                int l = q[1], r = q[2], x = 0;
                for (int i = l; i <= r; i++) x ^= a[i];
                ans.add(x);
            } else {
                a[q[1]] = q[2];
            }
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
