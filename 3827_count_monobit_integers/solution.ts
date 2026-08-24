// LeetCode 3827 - Count Monobit Integers
// https://leetcode.com/problems/count-monobit-integers/

export function countMonobit(n: any): any {
    let ans = 1;
    for (let i = 1, x = 1; x <= n; i++) {
        ans++;
        x += (1 << i);
    }
    return ans;
}
