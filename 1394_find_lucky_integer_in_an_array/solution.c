// LeetCode 1394 - Find Lucky Integer in an Array
// https://leetcode.com/problems/find-lucky-integer-in-an-array/

int findLucky(int* arr, int arrSize) {
    int cnt[501] = {0};
    for (int i = 0; i < arrSize; i++) if (arr[i] >= 1 && arr[i] <= 500) cnt[arr[i]]++;
    for (int x = 500; x >= 1; x--) if (cnt[x] == x) return x;
    return -1;
}
