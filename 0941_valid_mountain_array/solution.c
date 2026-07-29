// LeetCode 0941 - Valid Mountain Array
// https://leetcode.com/problems/valid-mountain-array/

#include <stdbool.h>

bool validMountainArray(int* arr, int arrSize) {
    if (arrSize < 3) return false;
    int i = 0;
    while (i + 1 < arrSize && arr[i] < arr[i + 1]) i++;
    if (i == 0 || i == arrSize - 1) return false;
    while (i + 1 < arrSize && arr[i] > arr[i + 1]) i++;
    return i == arrSize - 1;
}
