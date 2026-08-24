// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?
    public init() { self.val = 0; self.left = nil; self.right = nil }
    public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val; self.left = left; self.right = right
    }
}

class Solution {
    func treeQueries(_ root: TreeNode?, _ queries: [Int]) -> [Int] {
        var height = [Int: Int]()
        var level = [Int: Int]()
        var levelMax = [Int: [Int]]()
        func dfs(_ node: TreeNode?, _ d: Int) -> Int {
            guard let node else { return -1 }
            level[node.val] = d
            let h = 1 + max(dfs(node.left, d + 1), dfs(node.right, d + 1))
            height[node.val] = h
            var arr = levelMax[d, default: []]
            if arr.isEmpty {
                arr.append(h)
            } else if h >= arr[0] {
                if arr.count == 1 { arr.append(arr[0]) }
                else { arr[1] = arr[0] }
                arr[0] = h
            } else if arr.count == 1 || h > arr[1] {
                if arr.count == 1 { arr.append(h) }
                else { arr[1] = h }
            }
            levelMax[d] = arr
            return h
        }
        _ = dfs(root, 0)
        var ans = [Int](repeating: 0, count: queries.count)
        for i in 0..<queries.count {
            let q = queries[i]
            let d = level[q]!, h = height[q]!
            let top = levelMax[d]!
            if top[0] == h {
                ans[i] = top.count > 1 ? d + top[1] : d - 1
            } else {
                ans[i] = d + top[0]
            }
        }
        return ans
    }
}
