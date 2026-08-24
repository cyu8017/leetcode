// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

export function findEvenNumbers(digits: number[]): number[] {
    const freq = new Array(10).fill(0);
    for (const d of digits) freq[d]++;
    const ans = [];
    for (let x = 100; x <= 998; x += 2) {
        const a = Math.floor(x / 100), b = Math.floor(x / 10) % 10, c = x % 10;
        freq[a]--; freq[b]--; freq[c]--;
        if (freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0) ans.push(x);
        freq[a]++; freq[b]++; freq[c]++;
    }
    return ans;
}
