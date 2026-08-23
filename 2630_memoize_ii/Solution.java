// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

import java.util.*;
import java.util.function.Function;

// JavaScript problem; Java stand-in.
class Solution {
    public Function<int[], Integer> memoizeII(Function<int[], Integer> fn) {
        Map<String, Integer> cache = new HashMap<>();
        return args -> {
            StringBuilder sb = new StringBuilder();
            for (int a : args) {
                sb.append('|');
                sb.append(a);
            }
            String k = sb.toString();
            Integer v = cache.get(k);
            if (v != null) return v;
            v = fn.apply(args);
            cache.put(k, v);
            return v;
        };
    }
}
