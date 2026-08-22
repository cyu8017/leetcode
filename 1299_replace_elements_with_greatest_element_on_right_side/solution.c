// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

int* replaceElements(int* arr, int arrSize, int* returnSize) {
    int greatest = -1;
    for (int i = arrSize - 1; i >= 0; i--) {
        int cur = arr[i];
        arr[i] = greatest;
        if (cur > greatest) greatest = cur;
    }
    *returnSize = arrSize;
    return arr;
}
