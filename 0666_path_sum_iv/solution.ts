// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

export function pathSum(nums: number[]): number {
    const tree = new Map();
    const key = (depth, pos) => depth + "," + pos;
    let total = 0;
    for (const num of nums) {
        tree.set(key(Math.floor(num / 100), Math.floor(num / 10) % 10), num % 10);
    }
    const dfs = (depth, pos, path) => {
        const k = key(depth, pos);
        if (!tree.has(k)) return;
        path += tree.get(k);
        const left = key(depth + 1, pos * 2 - 1);
        const right = key(depth + 1, pos * 2);
        if (!tree.has(left) && !tree.has(right)) {
            total += path;
            return;
        }
        dfs(depth + 1, pos * 2 - 1, path);
        dfs(depth + 1, pos * 2, path);
    };
    dfs(1, 1, 0);
    return total;
}
