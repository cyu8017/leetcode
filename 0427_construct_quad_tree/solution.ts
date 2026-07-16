// LeetCode 0427 - Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/

export class Node {
    val: boolean;
    isLeaf: boolean;
    topLeft: Node | null;
    topRight: Node | null;
    bottomLeft: Node | null;
    bottomRight: Node | null;

    constructor(
        val: boolean = false,
        isLeaf: boolean = false,
        topLeft: Node | null = null,
        topRight: Node | null = null,
        bottomLeft: Node | null = null,
        bottomRight: Node | null = null,
    ) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
}

export class Solution {
    construct(grid: number[][]): Node {
        const build = (row: number, col: number, size: number): Node => {
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
