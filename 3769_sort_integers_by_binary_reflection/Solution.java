// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort_integers_by_binary_reflection/

import java.util.Arrays;

class Solution {
    public int[] sortByReflection(int[] nums) {
        Integer[] arr = new Integer[nums.length];
        for (int i = 0; i < nums.length; i++) arr[i] = nums[i];
        Arrays.sort(arr, (a, b) -> {
            int fa = f(a), fb = f(b);
            if (fa != fb) return Integer.compare(fa, fb);
            return Integer.compare(a, b);
        });
        for (int i = 0; i < nums.length; i++) nums[i] = arr[i];
        return nums;
    }

    private int f(int x) {
        int y = 0;
        while (x != 0) {
            y = (y << 1) | (x & 1);
            x >>= 1;
        }
        return y;
    }
}
