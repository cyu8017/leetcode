// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

export function numberOfEmployeesWhoMetTarget(hours: number[], target: number): number {
    let ans = 0;
    for (const h of hours) if (h >= target) ans++;
    return ans;
}
