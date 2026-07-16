class Node {
    var val: Int
    var next: Node?
    var random: Node?

    init(_ val: Int) {
        self.val = val
    }
}

class Solution {
    func copyRandomList(_ head: Node?) -> Node? {
        var clones = [ObjectIdentifier: Node]()

        func clone(_ node: Node?) -> Node? {
            guard let node = node else { return nil }
            let key = ObjectIdentifier(node)
            if let copy = clones[key] { return copy }

            let copy = Node(node.val)
            clones[key] = copy
            copy.next = clone(node.next)
            copy.random = clone(node.random)
            return copy
        }

        return clone(head)
    }
}