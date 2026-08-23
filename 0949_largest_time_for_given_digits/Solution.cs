// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

using System;

public class Solution {
    public string LargestTimeFromDigits(int[] arr) {
        Array.Sort(arr);
        string best = "";
        do {
            int hours = 10 * arr[0] + arr[1];
            int minutes = 10 * arr[2] + arr[3];
            if (hours < 24 && minutes < 60) {
                string cand = $"{hours:D2}:{minutes:D2}";
                if (string.CompareOrdinal(cand, best) > 0) best = cand;
            }
        } while (NextPermutation(arr));
        return best;
    }
    private bool NextPermutation(int[] a) {
        int i = a.Length - 2;
        while (i >= 0 && a[i] >= a[i + 1]) i--;
        if (i < 0) return false;
        int j = a.Length - 1;
        while (a[j] <= a[i]) j--;
        (a[i], a[j]) = (a[j], a[i]);
        Array.Reverse(a, i + 1, a.Length - i - 1);
        return true;
    }
}
