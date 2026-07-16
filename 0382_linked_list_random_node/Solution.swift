// LeetCode 0382 - Linked List Random Node
// https://leetcode.com/problems/linked-list-random-node/

class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    private var nodes: [ListNode] = []

    init(_ head: [Int]) {
        var current: ListNode? = buildList(head)
        while let node = current {
            nodes.append(node)
            current = node.next
        }
        srand48(327)
    }

    func getRandom() -> Int {
        nodes[Int(drand48() * Double(nodes.count))].val
    }

    private func buildList(_ values: [Int]) -> ListNode? {
        guard let first = values.first else {
            return nil
        }

        let head = ListNode(first)
        var current = head
        for value in values.dropFirst() {
            current.next = ListNode(value)
            current = current.next!
        }
        return head
    }
}
