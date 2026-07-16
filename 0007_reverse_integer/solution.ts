// LeetCode 0007 - Reverse Integer
// https://leetcode.com/problems/reverse-integer/

export function reverse(x: number): number {
    let result = 0;

    while (x !== 0) {
        const pop = x % 10;
        x = (x / 10) | 0;

        if (result > 2147483647 / 10 || (result === 2147483647 / 10 && pop > 7)) {
            return 0;
        }
        if (result < -2147483648 / 10 || (result === -2147483648 / 10 && pop < -8)) {
            return 0;
        }

        result = result * 10 + pop;
    }

    return result;
}
