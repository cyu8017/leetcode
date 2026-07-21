// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

public class Solution {
    public int GetMinSwaps(string num, int k) {
        char[] target = num.ToCharArray();
        for (int t = 0; t < k; t++) NextPermutation(target);

        char[] source = num.ToCharArray();
        int swaps = 0;
        for (int i = 0; i < source.Length; i++) {
            if (source[i] == target[i]) continue;
            int j = i;
            while (source[j] != target[i]) j++;
            while (j > i) {
                (source[j], source[j - 1]) = (source[j - 1], source[j]);
                swaps++;
                j--;
            }
        }
        return swaps;
    }

    private void NextPermutation(char[] arr) {
        int i = arr.Length - 2;
        while (i >= 0 && arr[i] >= arr[i + 1]) i--;
        if (i < 0) {
            System.Array.Reverse(arr);
            return;
        }
        int j = arr.Length - 1;
        while (arr[j] <= arr[i]) j--;
        (arr[i], arr[j]) = (arr[j], arr[i]);
        System.Array.Reverse(arr, i + 1, arr.Length - i - 1);
    }
}
