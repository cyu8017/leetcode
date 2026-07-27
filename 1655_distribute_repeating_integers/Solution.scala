// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

object Solution {
  def canDistribute(nums: Array[Int], quantity: Array[Int]): Boolean = {
    val cnt = nums.groupBy(identity).values.map(_.length).toArray
    val q = quantity.sorted.reverse
    val m = q.length
    val sums = Array.fill(1 << m)(0)
    var mask = 1
    while (mask < (1 << m)) {
      val bit = mask & -mask
      sums(mask) = sums(mask ^ bit) + q(Integer.numberOfTrailingZeros(bit))
      mask += 1
    }
    var dp = Set(0)
    for (c <- cnt) {
      val nxt = scala.collection.mutable.Set[Int]()
      for (mask <- dp) {
        nxt += mask
        val left = ((1 << m) - 1) ^ mask
        var sub = left
        while (sub > 0) {
          if (sums(sub) <= c) nxt += (mask | sub)
          sub = (sub - 1) & left
        }
      }
      dp = nxt.toSet
    }
    dp.contains((1 << m) - 1)
  }
}
