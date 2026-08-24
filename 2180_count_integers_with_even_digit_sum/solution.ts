// LeetCode 2180 - Count Integers With Even Digit Sum
// https://leetcode.com/problems/count-integers-with-even-digit-sum/

export function countEven(num: number): number {
    let ans = 0;
    for (let x = 1; x <= num; x++) {
        let s = 0, y = x;
        while (y > 0) { s += y % 10; y = Math.floor(y / 10); }
        if (s % 2 === 0) ans++;
    }
    return ans;
}
