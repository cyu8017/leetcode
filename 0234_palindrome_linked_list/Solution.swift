// LeetCode 0234 - Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func isPalindrome(_ head: ListNode?) -> Bool {
        guard let head, head.next != nil else {
            return true
        }

        var slow: ListNode? = head
        var fast: ListNode? = head
        while fast?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
        }

        var prev: ListNode? = nil
        var current = slow
        while let node = current {
            let next = node.next
            node.next = prev
            prev = node
            current = next
        }

        var left: ListNode? = head
        var right = prev
        while let rightNode = right {
            if left?.val != rightNode.val {
                return false
            }
            left = left?.next
            right = rightNode.next
        }
        return true
    }
}
