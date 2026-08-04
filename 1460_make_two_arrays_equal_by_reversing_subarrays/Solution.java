// LeetCode 1460 - Make Two Arrays Equal By Reversing Subarrays
// https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

import java.util.*;

class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        int[] a = target.clone(), b = arr.clone();
        Arrays.sort(a);
        Arrays.sort(b);
        return Arrays.equals(a, b);
    }
}
