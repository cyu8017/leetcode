// LeetCode 1483 - Kth Ancestor of a Tree Node
// https://leetcode.com/problems/kth-ancestor-of-a-tree-node/

class TreeAncestor {
    private var up: [[Int]]

    init(_ n: Int, _ parent: [Int]) {
        var width = 1
        var tmp = n
        while tmp > 1 { tmp >>= 1; width += 1 }
        up = [parent]
        for _ in 1..<width {
            let prev = up.last!
            up.append(prev.map { $0 == -1 ? -1 : prev[$0] })
        }
    }

    func getKthAncestor(_ node: Int, _ k: Int) -> Int {
        var node = node, k = k, bit = 0
        while k > 0 && node != -1 {
            if k & 1 != 0 {
                if bit >= up.count { return -1 }
                node = up[bit][node]
            }
            bit += 1
            k >>= 1
        }
        return node
    }
}
