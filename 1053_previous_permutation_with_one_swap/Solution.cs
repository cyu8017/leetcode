// LeetCode 1053 - Previous Permutation With One Swap
// https://leetcode.com/problems/previous-permutation-with-one-swap/

public class Solution {
    public int[] PrevPermOpt1(int[] arr) {
        int n = arr.Length;
        int i = n - 2;
        while (i >= 0 && arr[i] <= arr[i + 1]) {
            i--;
        }
        if (i < 0) {
            return arr;
        }
        int j = n - 1;
        while (arr[j] >= arr[i] || arr[j] == arr[j - 1]) {
            j--;
        }
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
        return arr;
    }
}
