class Node {
    var val: Int
    var neighbors: [Node]

    init(_ val: Int) {
        self.val = val
        self.neighbors = []
    }
}

class Solution {
    func cloneGraph(_ node: Node?) -> Node? {
        guard let node = node else { return nil }
        var clones = [ObjectIdentifier: Node]()

        func dfs(_ current: Node) -> Node {
            let key = ObjectIdentifier(current)
            if let clone = clones[key] { return clone }

            let clone = Node(current.val)
            clones[key] = clone
            clone.neighbors = current.neighbors.map { dfs($0) }
            return clone
        }

        return dfs(node)
    }
}