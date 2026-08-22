// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

typedef void (*ForEachCallback)(int value, int index, int* arr, int arrSize, void* context);

void forEach(int* arr, int arrSize, ForEachCallback callback, void* context) {
    for (int i = 0; i < arrSize; i++) {
        callback(arr[i], i, arr, arrSize, context);
    }
}
