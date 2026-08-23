// LeetCode 2724 - Sort By
// https://leetcode.com/problems/sort-by/

import java.util.*;
import java.util.function.IntToDoubleFunction;

// JS sortBy stand-in
class Solution {
    public int[] sortBy(int[] arr, IntToDoubleFunction fn) {
        Integer[] boxed = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(boxed, Comparator.comparingDouble(fn::applyAsDouble));
        int[] out = new int[boxed.length];
        for (int i = 0; i < boxed.length; i++) out[i] = boxed[i];
        return out;
    }
}
