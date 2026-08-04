// LeetCode 1442 - Count Triplets That Can Form Two Arrays Of Equal Xor
// https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

class Solution {
    public int countTriplets(int[] arr) {
        int answer = 0;
        for (int i = 0; i < arr.length; i++) {
            int value = 0;
            for (int k = i; k < arr.length; k++) {
                value ^= arr[k];
                if (value == 0) answer += k - i;
            }
        }
        return answer;
    }
}
