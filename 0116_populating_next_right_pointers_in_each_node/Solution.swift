class Node {
    var val: Int
    var left: Node?
    var right: Node?
    var next: Node?
    init() { self.val = 0; self.left = nil; self.right = nil; self.next = nil }
    init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; self.next = nil }
    init(_ val: Int, _ left: Node?, _ right: Node?, _ next: Node?) {
        self.val = val; self.left = left; self.right = right; self.next = next
    }
}

class Solution {
    func connect(_ root: Node?) -> Node? {
        guard let root = root else { return nil }
        var level = [root]
        while !level.isEmpty {
            for index in level.indices {
                level[index].next = index + 1 < level.count ? level[index + 1] : nil
            }
            level = level.flatMap { node in [node.left, node.right].compactMap { $0 } }
        }
        return root
    }
}