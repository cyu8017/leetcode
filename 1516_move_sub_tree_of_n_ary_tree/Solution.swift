// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

class Node {
    var val: Int
    var children: [Node]
    init(_ val: Int = 0, _ children: [Node] = []) {
        self.val = val
        self.children = children
    }
}

class Solution {
    func moveSubTree(_ root: Node?, _ p: Node?, _ q: Node?) -> Node? {
        guard var root = root, let p = p, let q = q else { return root }
        var parent = [ObjectIdentifier: Node]()
        func build(_ node: Node) {
            for child in node.children {
                parent[ObjectIdentifier(child)] = node
                build(child)
            }
        }
        build(root)
        if parent[ObjectIdentifier(p)] === q { return root }

        func isAncestor(_ a: Node, _ b: Node) -> Bool {
            var cur: Node? = b
            while let c = cur, let par = parent[ObjectIdentifier(c)] {
                if par === a { return true }
                cur = par
            }
            return false
        }

        let pParent = parent[ObjectIdentifier(p)]
        let qParent = parent[ObjectIdentifier(q)]

        if isAncestor(p, q) {
            if let qp = qParent, let idx = qp.children.firstIndex(where: { $0 === q }) {
                qp.children.remove(at: idx)
            }
            if pParent == nil {
                root = q
            } else if let pp = pParent, let idx = pp.children.firstIndex(where: { $0 === p }) {
                pp.children[idx] = q
            }
            q.children.append(p)
        } else {
            if pParent == nil {
                root = q
            } else if let pp = pParent, let idx = pp.children.firstIndex(where: { $0 === p }) {
                pp.children.remove(at: idx)
            }
            q.children.append(p)
        }
        return root
    }
}
