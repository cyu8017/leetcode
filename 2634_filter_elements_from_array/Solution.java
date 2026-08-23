// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

import java.util.*;
import java.util.function.BiPredicate;

// JavaScript problem; Java stand-in.
class Solution {
    public int[] filter(int[] arr, BiPredicate<Integer, Integer> fn) {
        List<Integer> out = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (fn.test(arr[i], i)) out.add(arr[i]);
        }
        int[] ans = new int[out.size()];
        for (int i = 0; i < out.size(); i++) ans[i] = out.get(i);
        return ans;
    }
}
