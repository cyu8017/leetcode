// LeetCode 1343 - Number Of Sub Arrays Of Size K And Average Greater Than Or Equal To Threshold
// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

public class Solution {
    public int NumOfSubarrays(int[] arr, int k, int threshold) {
        int window = 0;
        for (int i = 0; i < k; i++) window += arr[i];
        int answer = window >= k * threshold ? 1 : 0;
        for (int i = k; i < arr.Length; i++) {
            window += arr[i] - arr[i - k];
            if (window >= k * threshold) answer++;
        }
        return answer;
    }
}
