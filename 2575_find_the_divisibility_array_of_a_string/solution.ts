// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

export function divisibilityArray(word: string, m: number): number[] {
    const ans = new Array(word.length).fill(0);
    let cur = 0;
    for (let i = 0; i < word.length; ++i) {
        cur = (cur * 10 + (word.charCodeAt(i) - 48)) % m;
        if (cur === 0) ans[i] = 1;
    }
    return ans;
}
