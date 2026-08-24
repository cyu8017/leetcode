// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

class Solution {
    func isPreorder(_ nodes: [[Int]]) -> Bool {
        if nodes.isEmpty { return true }
        var stack: [Int] = [nodes[0][0]]
        for i in 1..<nodes.count {
            let id = nodes[i][0], parent = nodes[i][1]
            while !stack.isEmpty && stack.last != parent { stack.removeLast() }
            if stack.isEmpty { return false }
            stack.append(id)
        }
        return true
    }
}
