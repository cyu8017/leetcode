// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

export function maxValue(nums: any, k: any): any {
    const n = nums.length;
    const MAX = 128;
    const left = Array.from({length: n + 1}, () =>
        Array.from({length: k + 1}, () => new Array(MAX).fill(false)));
    left[0][0][0] = true;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j <= k; j++) {
            for (let v = 0; v < MAX; v++) {
                if (!left[i][j][v]) continue;
                left[i + 1][j][v] = true;
                if (j < k) left[i + 1][j + 1][v | nums[i]] = true;
            }
        }
    }
    const right = Array.from({length: n + 1}, () =>
        Array.from({length: k + 1}, () => new Array(MAX).fill(false)));
    right[n][0][0] = true;
    for (let i = n - 1; i >= 0; i--) {
        for (let j = 0; j <= k; j++) {
            for (let v = 0; v < MAX; v++) {
                if (!right[i + 1][j][v]) continue;
                right[i][j][v] = true;
                if (j < k) right[i][j + 1][v | nums[i]] = true;
            }
        }
    }
    let ans = 0;
    for (let mid = k; mid + k <= n; mid++) {
        for (let a = 0; a < MAX; a++) {
            if (!left[mid][k][a]) continue;
            for (let b = 0; b < MAX; b++) {
                if (right[mid][k][b] && (a ^ b) > ans) ans = a ^ b;
            }
        }
    }
    return ans;
}
