// LeetCode 1539 - Kth Missing Positive Number
// https://leetcode.com/problems/kth-missing-positive-number/

int findKthPositive(int* arr, int arrSize, int k) {
    int left = 0, right = arrSize;
    while (left < right) {
        int middle = (left + right) / 2;
        if (arr[middle] - middle - 1 < k) left = middle + 1;
        else right = middle;
    }
    return left + k;
}
