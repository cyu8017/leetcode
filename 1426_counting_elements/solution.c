// LeetCode 1426 - Counting Elements
// https://leetcode.com/problems/counting-elements/

int countElements(int* arr, int arrSize) {
    int seen[1002] = {0};
    for (int i = 0; i < arrSize; i++) seen[arr[i]] = 1;
    int ans = 0;
    for (int i = 0; i < arrSize; i++) if (seen[arr[i] + 1]) ans++;
    return ans;
}
