// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int minimumOperations(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for (int x : nums) list.add(x);
        int ops = 0;
        while (true) {
            Set<Integer> seen = new HashSet<>();
            boolean dup = false;
            for (int x : list) {
                if (!seen.add(x)) { dup = true; break; }
            }
            if (!dup) return ops;
            if (list.size() <= 3) return ops + 1;
            list.subList(0, 3).clear();
            ops++;
        }
    }
}
