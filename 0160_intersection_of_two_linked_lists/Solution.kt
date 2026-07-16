class ListNode(var `val`: Int = 0) { var next: ListNode? = null }

class Solution {
    fun getIntersectionNode(headA: ListNode?, headB: ListNode?): ListNode? {
        var a = headA; var b = headB
        while (a !== b) {
            a = a?.next ?: headB
            b = b?.next ?: headA
        }
        return a
    }
}