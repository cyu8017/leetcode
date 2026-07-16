// LeetCode 0069 - Sqrt(x)
// https://leetcode.com/problems/sqrtx/

export function mySqrt(x: number): number {
    if (x < 2) {
        return x;
    }

    let left = 2;
    let right = Math.floor(x / 2);

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const square = mid * mid;
        if (square === x) {
            return mid;
        }
        if (square < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return right;
}
