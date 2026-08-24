// LeetCode 2169 - Count Operations to Obtain Zero
// https://leetcode.com/problems/count-operations-to-obtain-zero/

export function countOperations(num1: number, num2: number): number {
    let ans = 0;
    while (num1 > 0 && num2 > 0) {
        if (num1 >= num2) { ans += Math.floor(num1 / num2); num1 %= num2; }
        else { ans += Math.floor(num2 / num1); num2 %= num1; }
    }
    return ans;
}
