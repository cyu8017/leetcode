// LeetCode 3316 - Find Maximum Removals From Source String
// https://leetcode.com/problems/find-maximum-removals-from-source-string/

function ok(removeFirst: any, source: any, pattern: any, targetIndices: any, n: any): any {
    const mark = new Array(n).fill(false);
    for (let i = 0; i < removeFirst; i++) mark[targetIndices[i]] = true;
    let j = 0;
    for (let i = 0; i < n && j < pattern.length; i++) {
        if (mark[i]) continue;
        if (source[i] === pattern[j]) j++;
    }
    return j === pattern.length;
}export function maxRemovals(source: any, pattern: any, targetIndices: any): any {
    const n = source.length;
    let lo = 0, hi = targetIndices.length;
    while (lo < hi) {
        const mid = (lo + hi + 1) >> 1;
        if (ok(mid, source, pattern, targetIndices, n)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
