// LeetCode 0427 - Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/

class Node {
    constructor(val = false, isLeaf = false, topLeft = null, topRight = null, bottomLeft = null, bottomRight = null) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
}

class Solution {
    construct(grid) {
        const build = (row, col, size) => {
            if (size === 1) {
                return new Node(Boolean(grid[row][col]), true);
            }

            const half = Math.floor(size / 2);
            const topLeft = build(row, col, half);
            const topRight = build(row, col + half, half);
            const bottomLeft = build(row + half, col, half);
            const bottomRight = build(row + half, col + half, half);

            if (
                topLeft.isLeaf
                && topRight.isLeaf
                && bottomLeft.isLeaf
                && bottomRight.isLeaf
                && topLeft.val === topRight.val
                && topLeft.val === bottomLeft.val
                && topLeft.val === bottomRight.val
            ) {
                return new Node(topLeft.val, true);
            }

            return new Node(true, false, topLeft, topRight, bottomLeft, bottomRight);
        };

        return build(0, 0, grid.length);
    }
}

module.exports = { Solution, Node };
