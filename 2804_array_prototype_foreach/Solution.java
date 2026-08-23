// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/
// JS-only problem; Java stand-in.

interface ArrayCallback {
    void call(int value, int index, int[] array);
}

class Solution {
    public void forEach(int[] arr, ArrayCallback callback) {
        for (int i = 0; i < arr.length; i++) callback.call(arr[i], i, arr);
    }
}
