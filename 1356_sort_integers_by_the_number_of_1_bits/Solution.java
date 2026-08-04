// LeetCode 1356 - Sort Integers By The Number Of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

import java.util.*;

class Solution {
    public int[] sortByBits(int[] arr) {
        Integer[] boxed = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(boxed, (a, b) -> {
            int ca = Integer.bitCount(a), cb = Integer.bitCount(b);
            return ca != cb ? Integer.compare(ca, cb) : Integer.compare(a, b);
        });
        for (int i = 0; i < arr.length; i++) arr[i] = boxed[i];
        return arr;
    }
}
