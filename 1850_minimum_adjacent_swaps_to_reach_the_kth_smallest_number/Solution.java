// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

class Solution {
    public int getMinSwaps(String num, int k) {
        char[] target = num.toCharArray();
        for (int i = 0; i < k; i++) {
            nextPermutation(target);
        }

        char[] source = num.toCharArray();
        int swaps = 0;
        for (int i = 0; i < source.length; i++) {
            if (source[i] == target[i]) {
                continue;
            }

            int j = i;
            while (source[j] != target[i]) {
                j++;
            }

            while (j > i) {
                swap(source, j, j - 1);
                swaps++;
                j--;
            }
        }

        return swaps;
    }

    private void nextPermutation(char[] arr) {
        int i = arr.length - 2;
        while (i >= 0 && arr[i] >= arr[i + 1]) {
            i--;
        }
        if (i < 0) {
            reverse(arr, 0, arr.length - 1);
            return;
        }

        int j = arr.length - 1;
        while (arr[j] <= arr[i]) {
            j--;
        }
        swap(arr, i, j);
        reverse(arr, i + 1, arr.length - 1);
    }

    private void reverse(char[] arr, int left, int right) {
        while (left < right) {
            swap(arr, left, right);
            left++;
            right--;
        }
    }

    private void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
