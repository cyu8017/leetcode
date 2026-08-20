// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

class Solution {
    func maxDepthBST(_ order: [Int]) -> Int {
        var nodes: [(Int, Int)] = []
        var ans = 0
        for value in order {
            var lo = 0, hi = nodes.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if nodes[mid].0 < value { lo = mid + 1 } else { hi = mid }
            }
            var depth = 1
            if lo > 0 { depth = max(depth, nodes[lo - 1].1 + 1) }
            if lo < nodes.count { depth = max(depth, nodes[lo].1 + 1) }
            nodes.insert((value, depth), at: lo)
            ans = max(ans, depth)
        }
        return ans
    }
}
