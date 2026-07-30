// LeetCode 1442 - Count Triplets That Can Form Two Arrays Of Equal Xor
// https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

public class Solution {
    public int CountTriplets(int[] arr) {
        int answer = 0;
        for (int i = 0; i < arr.Length; i++) {
            int value = 0;
            for (int k = i; k < arr.Length; k++) {
                value ^= arr[k];
                if (value == 0) answer += k - i;
            }
        }
        return answer;
    }
}
