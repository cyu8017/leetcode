// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

export function kthPalindrome(queries: number[], intLength: number): number[] {
    const half = (intLength + 1) >> 1;
    let start = 1;
    for (let i = 1; i < half; i++) start *= 10;
    const total = start * 9;
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const q = queries[i];
        if (q > total) { ans[i] = -1; continue; }
        let left = start + q - 1;
        let pal = left;
        let x = left;
        if (intLength % 2 !== 0) x = Math.floor(x / 10);
        while (x > 0) { pal = pal * 10 + x % 10; x = Math.floor(x / 10); }
        ans[i] = pal;
    }
    return ans;
}
