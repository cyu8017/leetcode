// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

export function calculateTax(brackets: any, income: any): any {
    let ans = 0, prev = 0;
    for (const b of brackets) {
        const upper = b[0], percent = b[1];
        if (income <= prev) break;
        const taxable = (income < upper) ? income - prev : upper - prev;
        ans += taxable * percent / 100.0;
        prev = upper;
    }
    return ans;
}
