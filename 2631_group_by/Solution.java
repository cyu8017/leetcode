// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/

import java.util.*;
import java.util.function.IntFunction;

// JavaScript problem; Java stand-in.
class Solution {
    public Map<String, List<Integer>> groupBy(int[] arr, IntFunction<String> fn) {
        Map<String, List<Integer>> out = new HashMap<>();
        for (int x : arr) {
            String k = fn.apply(x);
            out.computeIfAbsent(k, z -> new ArrayList<>()).add(x);
        }
        return out;
    }
}
