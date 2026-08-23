// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/
// JS-only problem; Java stand-in with Integer.MIN_VALUE as placeholder.

import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;
import java.util.function.ToIntFunction;

class Solution {
    public ToIntFunction<int[]> partial(ToIntFunction<int[]> fn, int[] args) {
        return rest -> {
            List<Integer> full = new ArrayList<>();
            int ri = 0;
            for (int a : args) {
                if (a == Integer.MIN_VALUE) {
                    if (ri < rest.length) full.add(rest[ri++]);
                } else {
                    full.add(a);
                }
            }
            while (ri < rest.length) full.add(rest[ri++]);
            int[] arr = new int[full.size()];
            for (int i = 0; i < full.size(); i++) arr[i] = full.get(i);
            return fn.applyAsInt(arr);
        };
    }
}
