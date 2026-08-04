// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution {
    public int[] replaceElements(int[] arr) {
        int greatest = -1;
        for (int i = arr.length - 1; i >= 0; i--) {
            int current = arr[i];
            arr[i] = greatest;
            greatest = Math.max(greatest, current);
        }
        return arr;
    }
}
