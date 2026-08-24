// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func gameResult(_ head: ListNode?) -> String {
        var odd = 0, even = 0
        var node = head
        while let cur = node, let nxt = cur.next {
            if cur.val < nxt.val { odd += 1 }
            if cur.val > nxt.val { even += 1 }
            node = nxt.next
        }
        if odd > even { return "Odd" }
        if odd < even { return "Even" }
        return "Tie"
    }
}
