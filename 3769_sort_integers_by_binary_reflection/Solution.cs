// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

using System;

public class Solution {
    public int[] SortByReflection(int[] nums) {
        int F(int x) {
            int y = 0;
            while (x != 0) {
                y = (y << 1) | (x & 1);
                x >>= 1;
            }
            return y;
        }
        Array.Sort(nums, (a, b) => {
            int fa = F(a), fb = F(b);
            if (fa != fb) return fa.CompareTo(fb);
            return a.CompareTo(b);
        });
        return nums;
    }
}
