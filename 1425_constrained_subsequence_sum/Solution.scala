import scala.collection.mutable
object Solution {
  def constrainedSubsetSum(nums: Array[Int], k: Int): Int = {
    val deque = mutable.ArrayDeque.empty[Int]
    val best = nums.clone()
    for (i <- nums.indices) {
      while (deque.nonEmpty && deque.head < i - k) deque.removeHead()
      best(i) = nums(i) + (if (deque.isEmpty) 0 else best(deque.head).max(0))
      while (deque.nonEmpty && best(deque.last) <= best(i)) deque.removeLast()
      deque.append(i)
    }
    best.max
  }
}
