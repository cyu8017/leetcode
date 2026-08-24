// LeetCode 0845 - Longest Mountain in Array
// https://leetcode.com/problems/longest-mountain-in-array/

export function longestMountain(arr: number[]): number {
    const n = arr.length;
    let ans = 0, i = 0;
    while (i < n) {
        let j = i;
        if (j + 1 < n && arr[j] < arr[j + 1]) {
            while (j + 1 < n && arr[j] < arr[j + 1]) j++;
            if (j + 1 < n && arr[j] > arr[j + 1]) {
                while (j + 1 < n && arr[j] > arr[j + 1]) j++;
                ans = Math.max(ans, j - i + 1);
                i = j;
                continue;
            }
        }
        i++;
    }
    return ans;
}
