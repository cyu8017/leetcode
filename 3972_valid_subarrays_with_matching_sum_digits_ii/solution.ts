// LeetCode 3972 - Valid Subarrays With Matching Sum Digits II
// https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-ii/

export function countValidSubarrays(nums: any, x: any): any {
    const byRemainder = Array.from({length: 10}, () => []);
    byRemainder[0].push(0);
    let prefix = 0, answer = 0;
    for (const value of nums) {
        prefix += value;
        const required = ((prefix - x) % 10 + 10) % 10;
        const values = byRemainder[required];
        for (let power = 1; x * power <= prefix; power *= 10) {
            const low = x * power;
            const high = (x + 1) * power - 1;
            const minPrefix = prefix - high, maxPrefix = prefix - low;
            const left = lowerBound(values, minPrefix);
            const right = upperBound(values, maxPrefix);
            answer += right - left;
            if (power > Math.floor(prefix / 10)) break;
        }
        byRemainder[prefix % 10].push(prefix);
    }
    return answer;
}
function lowerBound(a: any, x: any): any {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >>> 1;
        if (a[mid] < x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
function upperBound(a: any, x: any): any {
    let lo = 0, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >>> 1;
        if (a[mid] <= x) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
