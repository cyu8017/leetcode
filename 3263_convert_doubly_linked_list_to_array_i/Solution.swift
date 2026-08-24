// LeetCode 3263 - Convert Doubly Linked List to Array I
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-i/

class Node {
    var val: Int
    var prev: Node?
    var next: Node?
    init(_ val: Int) {
        self.val = val
        self.prev = nil
        self.next = nil
    }
}

class Solution {
    func toArray(_ head: Node?) -> [Int] {
        var ans: [Int] = []
        var node = head
        while let cur = node {
            ans.append(cur.val)
            node = cur.next
        }
        return ans
    }
}
