// LeetCode 0328 - Odd Even Linked List
// https://leetcode.com/problems/odd-even-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func oddEvenList(_ head: ListNode?) -> ListNode? {
        guard let head, head.next != nil else {
            return head
        }

        var odd: ListNode? = head
        var even = head.next
        let evenHead = even
        while even?.next != nil {
            odd?.next = even?.next
            odd = odd?.next
            even?.next = odd?.next
            even = even?.next
        }
        odd?.next = evenHead
        return head
    }
}
