// LeetCode 1687 - Delivering Boxes from Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

object Solution {
  def boxDelivering(boxes: Array[Array[Int]], portsCount: Int, maxBoxes: Int, maxWeight: Int): Int = {
    val n = boxes.length
    val w = Array.fill(n + 1)(0)
    val changes = Array.fill(n + 1)(0)
    for (i <- 1 to n) {
      w(i) = w(i - 1) + boxes(i - 1)(1)
      changes(i) = changes(i - 1)
      if (i > 1 && boxes(i - 1)(0) != boxes(i - 2)(0)) changes(i) += 1
    }
    val dp = Array.fill(n + 1)(0)
    val q = scala.collection.mutable.ArrayBuffer(0)
    for (i <- 1 to n) {
      while (q.nonEmpty && (i - q(0) > maxBoxes || w(i) - w(q(0)) > maxWeight)) {
        q.remove(0)
      }
      val j = q(0)
      dp(i) = dp(j) + changes(i) - changes(j + 1) + 2
      if (i < n) {
        val value = dp(i) - changes(i + 1)
        while (q.nonEmpty && dp(q.last) - changes(q.last + 1) >= value) {
          q.remove(q.length - 1)
        }
        q += i
      }
    }
    dp(n)
  }
}
