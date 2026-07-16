class ListNode(var x: Int = 0) { var next: ListNode = null }

object Solution {
  def getIntersectionNode(headA: ListNode, headB: ListNode): ListNode = {
    var a = headA; var b = headB
    while (a ne b) {
      a = if (a == null) headB else a.next
      b = if (b == null) headA else b.next
    }
    a
  }
}