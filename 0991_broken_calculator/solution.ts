// LeetCode 0991 - Broken Calculator
// https://leetcode.com/problems/broken-calculator/

export function brokenCalc(startValue: number, target: number): number {
    let ans = 0;
    while (target > startValue) {
        if (target % 2 === 1) target++;
        else target = Math.floor(target / 2);
        ans++;
    }
    return ans + startValue - target;
}
