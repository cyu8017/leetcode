// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

public class Node {
    public var val: Int
    public var prev: Node?
    public var next: Node?
    public init() { self.val = 0; self.prev = nil; self.next = nil }
    public init(_ val: Int) { self.val = val; self.prev = nil; self.next = nil }
}

class Solution {
    func toArray(_ node: Node?) -> [Int] {
        var node = node
        while node?.prev != nil { node = node?.prev }
        var ans = [Int]()
        while let cur = node {
            ans.append(cur.val)
            node = cur.next
        }
        return ans
    }
}
