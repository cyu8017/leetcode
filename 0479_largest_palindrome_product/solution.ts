// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

export class Solution {
    largestPalindrome(n: number): number {
        if (n === 1) return 9;
        const upper = 10 ** n - 1;
        const lower = 10 ** (n - 1);
        for (let first = upper; first >= lower; first -= 1) {
            const candidate = Number(`${first}${String(first).split("").reverse().join("")}`);
            let factor = upper;
            while (factor * factor >= candidate) {
                if (candidate % factor === 0) {
                    const other = candidate / factor;
                    if (other >= lower && other <= upper) {
                        return candidate % 1337;
                    }
                }
                factor -= 1;
            }
        }
        return 0;
    }
}
