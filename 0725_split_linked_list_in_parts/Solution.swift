// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func splitListToParts(_ head: ListNode?, _ k: Int) -> [ListNode?] {
        var len = 0
        var cur = head
        while cur != nil { len += 1; cur = cur?.next }
        let base = len / k, extra = len % k
        var result = [ListNode?](repeating: nil, count: k)
        cur = head
        for i in 0..<k {
            result[i] = cur
            let size = base + (i < extra ? 1 : 0)
            if size == 0 { continue }
            for _ in 0..<(size - 1) { cur = cur?.next }
            let next = cur?.next
            cur?.next = nil
            cur = next
        }
        return result
    }
}
