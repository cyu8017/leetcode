// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

function lis(a: any): any {
    const tails = [];
    for (const x of a) {
        let lo = 0, hi = tails.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (tails[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        if (lo === tails.length) tails.push(x);
        else tails[lo] = x;
    }
    return tails.length;
}export function maxPathLength(coordinates: any, k: any): any {
    const n = coordinates.length;
    const arr = Array.from({length: n}, (_, i) => [coordinates[i][0], coordinates[i][1], i]);
    arr.sort((a, b) => a[0] === b[0] ? b[1] - a[1] : a[0] - b[0]);
    const kx = coordinates[k][0], ky = coordinates[k][1];
    const left = [], right = [];
    for (const p of arr) {
        if (p[0] < kx && p[1] < ky) left.push(p[1]);
        if (p[0] > kx && p[1] > ky) right.push(p[1]);
    }
    return lis(left) + 1 + lis(right);
}
