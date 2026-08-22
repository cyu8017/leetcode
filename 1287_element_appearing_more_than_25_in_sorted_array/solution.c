// LeetCode 1287 - Element Appearing More Than 25% In Sorted Array
// https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

int findSpecialInteger(int* arr, int arrSize) {
    int limit = arrSize / 4;
    int candidates[3] = {arr[arrSize / 4], arr[arrSize / 2], arr[3 * arrSize / 4]};
    for (int c = 0; c < 3; c++) {
        int value = candidates[c], count = 0;
        for (int i = 0; i < arrSize; i++) if (arr[i] == value) count++;
        if (count > limit) return value;
    }
    return arr[0];
}
