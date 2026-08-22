// LeetCode 1588 - Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

int sumOddLengthSubarrays(int* arr, int arrSize) {
    int ans = 0;
    for (int i = 0; i < arrSize; i++) {
        ans += arr[i] * (((i + 1) * (arrSize - i) + 1) / 2);
    }
    return ans;
}
