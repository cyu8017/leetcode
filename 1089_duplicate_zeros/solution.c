// LeetCode 1089 - Duplicate Zeros
// https://leetcode.com/problems/duplicate-zeros/

void duplicateZeros(int* arr, int arrSize) {
    int zeros = 0;
    for (int i = 0; i < arrSize; i++) {
        if (arr[i] == 0) {
            zeros++;
        }
    }
    for (int i = arrSize - 1; i >= 0; i--) {
        if (i + zeros < arrSize) {
            arr[i + zeros] = arr[i];
        }
        if (arr[i] == 0) {
            zeros--;
            if (i + zeros < arrSize) {
                arr[i + zeros] = 0;
            }
        }
    }
}
