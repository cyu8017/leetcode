// LeetCode 3780 - Maximum Sum Of Three Numbers Divisible By Three
// https://leetcode.com/problems/maximum_sum_of_three_numbers_divisible_by_three/

export function maximumSum(nums: any): any {
    const a = nums.slice().sort((x, y) => x - y);
    const g = [[], [], []];
    for (const x of a) g[x % 3].push(x);
    let ans = 0;
    for (let aa = 0; aa < 3; aa++) {
        if (g[aa].length) {
            const x = g[aa].pop();
            for (let b = 0; b < 3; b++) {
                if (g[b].length) {
                    const y = g[b].pop();
                    const c = (3 - (aa + b) % 3) % 3;
                    if (g[c].length) {
                        const z = g[c][g[c].length - 1];
                        ans = Math.max(ans, x + y + z);
                    }
                    g[b].push(y);
                }
            }
            g[aa].push(x);
        }
    }
    return ans;
}
