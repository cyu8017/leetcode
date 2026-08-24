// LeetCode 3219 - Minimum Cost for Cutting Cake II
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/

export function minimumCost(m: any, n: any, horizontalCut: any, verticalCut: any): any {
    horizontalCut.sort((a, b) => b - a);
    verticalCut.sort((a, b) => b - a);
    let i = 0, j = 0, h = 1, v = 1, ans = 0;
    while (i < m - 1 || j < n - 1) {
        if (j === n - 1 || (i < m - 1 && horizontalCut[i] > verticalCut[j])) {
            ans += horizontalCut[i] * v;
            h++; i++;
        } else {
            ans += verticalCut[j] * h;
            v++; j++;
        }
    }
    return ans;
}
