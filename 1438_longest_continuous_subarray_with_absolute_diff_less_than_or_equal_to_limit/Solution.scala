import scala.collection.mutable
object Solution {
  def longestSubarray(nums: Array[Int], limit: Int): Int = {
    val low = mutable.ArrayDeque.empty[Int]; val high = mutable.ArrayDeque.empty[Int]
    var left = 0; var answer = 0
    for (right <- nums.indices) {
      while (low.nonEmpty && nums(low.last) > nums(right)) low.removeLast()
      while (high.nonEmpty && nums(high.last) < nums(right)) high.removeLast()
      low.append(right); high.append(right)
      while (nums(high.head) - nums(low.head) > limit) {
        left += 1
        if (low.head < left) low.removeHead()
        if (high.head < left) high.removeHead()
      }
      answer = answer.max(right - left + 1)
    }
    answer
  }
}
