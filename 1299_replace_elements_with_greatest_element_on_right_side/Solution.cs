// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

public class Solution {
    public int[] ReplaceElements(int[] arr) {
        int greatest = -1;
        for (int i = arr.Length - 1; i >= 0; i--) {
            int current = arr[i];
            arr[i] = greatest;
            greatest = System.Math.Max(greatest, current);
        }
        return arr;
    }
}
