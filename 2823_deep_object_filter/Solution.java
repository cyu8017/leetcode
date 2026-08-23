// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/
// JS-only problem; Java vector filter stand-in.

import java.util.ArrayList;
import java.util.List;
import java.util.function.IntPredicate;

class Solution {
    public List<Integer> deepFilter(int[] obj, IntPredicate fn) {
        List<Integer> output = new ArrayList<>();
        for (int v : obj) if (fn.test(v)) output.add(v);
        return output;
    }
}
