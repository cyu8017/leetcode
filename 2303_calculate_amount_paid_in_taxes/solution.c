// LeetCode 2303 - Calculate Amount Paid in Taxes
// https://leetcode.com/problems/calculate-amount-paid-in-taxes/

double calculateTax(int** brackets, int bracketsSize, int* bracketsColSize, int income) {
    (void)bracketsColSize;
    double ans = 0.0;
    int prev = 0;
    for (int i = 0; i < bracketsSize; i++) {
        int upper = brackets[i][0], percent = brackets[i][1];
        if (income <= prev) break;
        int taxable = upper - prev;
        if (income < upper) taxable = income - prev;
        ans += (double)taxable * (double)percent / 100.0;
        prev = upper;
    }
    return ans;
}
