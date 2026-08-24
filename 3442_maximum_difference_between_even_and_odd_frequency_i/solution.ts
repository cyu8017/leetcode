// LeetCode 3442 - Maximum Difference Between Even and Odd Frequency I
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

export function maxDifference(s: any): any {
    const freq = new Array(26).fill(0);
    for (const c of s) freq[c.charCodeAt(0) - 97]++;
    let maxOdd = 0, minEven = 1e9;
    for (const f of freq) {
        if (f === 0) continue;
        if (f % 2 === 1) {
            if (f > maxOdd) maxOdd = f;
        } else if (f < minEven) minEven = f;
    }
    return maxOdd - minEven;
}
