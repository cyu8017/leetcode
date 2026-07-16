// LeetCode 0445 - Add Two Numbers II
// https://leetcode.com/problems/add-two-numbers-ii/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        var stack1: [Int] = []
        var stack2: [Int] = []
        var node1 = l1
        var node2 = l2
        while let n1 = node1 {
            stack1.append(n1.val)
            node1 = n1.next
        }
        while let n2 = node2 {
            stack2.append(n2.val)
            node2 = n2.next
        }

        var carry = 0
        var head: ListNode? = nil
        while !stack1.isEmpty || !stack2.isEmpty || carry != 0 {
            var total = carry
            if !stack1.isEmpty {
                total += stack1.removeLast()
            }
            if !stack2.isEmpty {
                total += stack2.removeLast()
            }
            carry = total / 10
            let node = ListNode(total % 10, head)
            head = node
        }
        return head
    }
}
