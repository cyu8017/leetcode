// LeetCode 1524 - Number of Sub-arrays With Odd Sum
// https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

int numOfSubarrays(int* arr, int arrSize) {
    int counts[2] = {1, 0};
    int parity = 0;
    long long answer = 0;
    for (int i = 0; i < arrSize; i++) {
        parity ^= arr[i] & 1;
        answer += counts[parity ^ 1];
        counts[parity]++;
    }
    return (int)(answer % 1000000007LL);
}
