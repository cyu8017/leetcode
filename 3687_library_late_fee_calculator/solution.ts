// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

export function lateFee(daysLate: any): any {
    const fee = (x) => {
        if (x === 1) return 1;
        if (x > 5) return 3 * x;
        return 2 * x;
    };
    let ans = 0;
    for (const x of daysLate) ans += fee(x);
    return ans;
}
