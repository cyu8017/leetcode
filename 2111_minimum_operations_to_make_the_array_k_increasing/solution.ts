// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

export function kIncreasing(arr: number[], k: number): number {
    let ans = 0;
    const n = arr.length;
    for (let start = 0; start < k; start++) {
        const seq = [];
        for (let i = start; i < n; i += k) seq.push(arr[i]);
        const tails = [];
        for (const x of seq) {
            let lo = 0, hi = tails.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (tails[mid] <= x) lo = mid + 1;
                else hi = mid;
            }
            if (lo === tails.length) tails.push(x);
            else tails[lo] = x;
        }
        ans += seq.length - tails.length;
    }
    return ans;
}
