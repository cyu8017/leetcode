// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

#define MAX(a,b) ((a)>(b)?(a):(b))

int longestMountain(int* arr, int arrSize) {
    int n = arrSize, ans = 0, i = 0;
    while (i < n) {
        int j = i;
        if (j + 1 < n && arr[j] < arr[j + 1]) {
            while (j + 1 < n && arr[j] < arr[j + 1]) j++;
            if (j + 1 < n && arr[j] > arr[j + 1]) {
                while (j + 1 < n && arr[j] > arr[j + 1]) j++;
                ans = MAX(ans, j - i + 1);
                i = j;
                continue;
            }
        }
        i++;
    }
    return ans;
}
