object Solution {
  def deleteNodes(head: ListNode, m: Int, n: Int): ListNode = {
    var current = head
    while (current != null) {
      var kept = 1
      while (kept < m && current != null) {
        current = current.next
        kept += 1
      }
      if (current != null) {
        var dropped = current.next
        var count = 0
        while (count < n && dropped != null) {
          dropped = dropped.next
          count += 1
        }
        current.next = dropped
        current = dropped
      }
    }
    head
  }
}
