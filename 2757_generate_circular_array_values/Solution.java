// LeetCode 2757 - Generate Circular Array Values
// https://leetcode.com/problems/generate-circular-array-values/
// JS generator stand-in.

import java.util.function.IntSupplier;

class Solution {
    public IntSupplier cyclicGenerator(int[] arr, int startIndex) {
        return new IntSupplier() {
            int i = startIndex;
            final int n = arr.length;
            public int getAsInt() {
                int v = arr[i];
                i = (i + 1) % n;
                return v;
            }
        };
    }
}
