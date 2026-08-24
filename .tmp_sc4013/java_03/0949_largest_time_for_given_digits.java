// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

import java.util.Arrays;

class Solution {
    public String largestTimeFromDigits(int[] arr) {
        Arrays.sort(arr);
        String best = "";
        do {
            int hours = 10 * arr[0] + arr[1];
            int minutes = 10 * arr[2] + arr[3];
            if (hours < 24 && minutes < 60) {
                String cand = String.format("%02d:%02d", hours, minutes);
                if (cand.compareTo(best) > 0) best = cand;
            }
        } while (nextPermutation(arr));
        return best;
    }

    private boolean nextPermutation(int[] a) {
        int i = a.length - 2;
        while (i >= 0 && a[i] >= a[i + 1]) i--;
        if (i < 0) return false;
        int j = a.length - 1;
        while (a[j] <= a[i]) j--;
        int tmp = a[i]; a[i] = a[j]; a[j] = tmp;
        for (int l = i + 1, r = a.length - 1; l < r; l++, r--) {
            tmp = a[l]; a[l] = a[r]; a[r] = tmp;
        }
        return true;
    }
}
