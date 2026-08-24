// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

export function maxWalls(robots: any, distance: any, walls: any): any {
    const n = robots.length;
    const arr = Array.from({length: n}, (_, i) => [robots[i], distance[i]]);
    arr.sort((a, b) => a[0] - b[0]);
    walls = walls.slice().sort((a, b) => a - b);
    const lowerBound = (a, target) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const memo = new Map();
    const dfs = (i, j) => {
        if (i < 0) return 0;
        const key = (i << 1) | j;
        if (memo.has(key)) return memo.get(key);
        let left = arr[i][0] - arr[i][1];
        if (i > 0) left = Math.max(left, arr[i - 1][0] + 1);
        let l = lowerBound(walls, left);
        let r = lowerBound(walls, arr[i][0] + 1);
        let ans = dfs(i - 1, 0) + (r - l);
        let right = arr[i][0] + arr[i][1];
        if (i + 1 < arr.length) {
            if (j === 0) right = Math.min(right, arr[i + 1][0] - arr[i + 1][1] - 1);
            else right = Math.min(right, arr[i + 1][0] - 1);
        }
        l = lowerBound(walls, arr[i][0]);
        r = lowerBound(walls, right + 1);
        ans = Math.max(ans, dfs(i - 1, 1) + (r - l));
        memo.set(key, ans);
        return ans;
    };
    return dfs(n - 1, 1);
}
