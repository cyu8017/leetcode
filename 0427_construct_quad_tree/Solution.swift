// LeetCode 0427 - Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/

class Node {
    var val: Bool
    var isLeaf: Bool
    var topLeft: Node?
    var topRight: Node?
    var bottomLeft: Node?
    var bottomRight: Node?

    init(
        _ val: Bool = false,
        _ isLeaf: Bool = false,
        _ topLeft: Node? = nil,
        _ topRight: Node? = nil,
        _ bottomLeft: Node? = nil,
        _ bottomRight: Node? = nil
    ) {
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
    }
}

class Solution {
    func construct(_ grid: [[Int]]) -> Node? {
        return build(grid, 0, 0, grid.count)
    }

    private func build(_ grid: [[Int]], _ row: Int, _ col: Int, _ size: Int) -> Node {
        if size == 1 {
            return Node(grid[row][col] == 1, true)
        }

        let half = size / 2
        let topLeft = build(grid, row, col, half)
        let topRight = build(grid, row, col + half, half)
        let bottomLeft = build(grid, row + half, col, half)
        let bottomRight = build(grid, row + half, col + half, half)

        if topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf &&
            topLeft.val == topRight.val && topLeft.val == bottomLeft.val && topLeft.val == bottomRight.val {
            return Node(topLeft.val, true)
        }

        return Node(true, false, topLeft, topRight, bottomLeft, bottomRight)
    }
}
