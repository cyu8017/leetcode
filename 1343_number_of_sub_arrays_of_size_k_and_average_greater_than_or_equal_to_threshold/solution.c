// LeetCode 1343 - Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

int numOfSubarrays(int* arr, int arrSize, int k, int threshold) {
    long window = 0;
    for (int i = 0; i < k; i++) window += arr[i];
    int answer = window >= (long)k * threshold;
    for (int i = k; i < arrSize; i++) {
        window += arr[i] - arr[i - k];
        answer += window >= (long)k * threshold;
    }
    return answer;
}
