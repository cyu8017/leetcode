// LeetCode 2520 - Count the Digits That Divide a Number
// https://leetcode.com/problems/count-the-digits-that-divide-a-number/

export function countDigits(num: number): number {
    let ans = 0, x = num;
    while (x > 0) {
        const d = x % 10;
        if (d !== 0 && num % d === 0) ans++;
        x = Math.floor(x / 10);
    }
    return ans;
}
