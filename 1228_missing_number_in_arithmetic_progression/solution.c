// LeetCode 1228 - Missing Number In Arithmetic Progression
// https://leetcode.com/problems/missing-number-in-arithmetic-progression/

int missingNumber(int* arr, int arrSize) {
    int diff = (arr[arrSize - 1] - arr[0]) / arrSize;
    for (int i = 1; i < arrSize; i++) {
        int expected = arr[0] + i * diff;
        if (arr[i] != expected) return expected;
    }
    return arr[0];
}
