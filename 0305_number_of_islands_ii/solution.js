// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} positions
 * @return {number[]}
 */
var numIslands2 = function(m, n, positions) {
    const parent = new Map();
    const rank = new Map();

    function find(index) {
        if (!parent.has(index)) {
            parent.set(index, index);
            rank.set(index, 0);
        }
        if (parent.get(index) !== index) {
            parent.set(index, find(parent.get(index)));
        }
        return parent.get(index);
    }

    function union(left, right) {
        const rootLeft = find(left);
        const rootRight = find(right);
        if (rootLeft === rootRight) {
            return false;
        }
        if (rank.get(rootLeft) < rank.get(rootRight)) {
            parent.set(rootLeft, rootRight);
        } else {
            parent.set(rootRight, rootLeft);
            if (rank.get(rootLeft) === rank.get(rootRight)) {
                rank.set(rootLeft, rank.get(rootLeft) + 1);
            }
        }
        return true;
    }

    const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    const result = [];
    let islands = 0;
    for (const [row, col] of positions) {
        const index = row * n + col;
        if (parent.has(index)) {
            result.push(islands);
            continue;
        }
        parent.set(index, index);
        islands += 1;
        for (const [dr, dc] of directions) {
            const nr = row + dr;
            const nc = col + dc;
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                const neighbor = nr * n + nc;
                if (parent.has(neighbor) && union(index, neighbor)) {
                    islands -= 1;
                }
            }
        }
        result.push(islands);
    }
    return result;
};
