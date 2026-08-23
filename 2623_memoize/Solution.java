// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

import java.util.*;
import java.util.function.IntUnaryOperator;

// JavaScript problem; Java stand-in.
class Solution {
    public IntUnaryOperator memoize(IntUnaryOperator fn) {
        Map<Integer, Integer> cache = new HashMap<>();
        return x -> {
            Integer v = cache.get(x);
            if (v != null) return v;
            int r = fn.applyAsInt(x);
            cache.put(x, r);
            return r;
        };
    }
}
