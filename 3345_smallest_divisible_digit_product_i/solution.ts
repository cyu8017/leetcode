// LeetCode 3345 - Smallest Divisible Digit Product I
// https://leetcode.com/problems/smallest-divisible-digit-product-i/

export function smallestNumber(n: any, t: any): any {
    for (let x = n; ; x++) {
        let p = 1, y = x;
        while (y > 0) {
            p *= y % 10;
            y = Math.floor(y / 10);
        }
        if (p % t === 0) return x;
    }
}
