// LeetCode 3678 - Smallest Absent Positive Greater Than Average
// https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

object Solution {
  def smallestAbsent(nums: Array[Int]): Int = {
    val s = new java.util.HashSet[Integer]()
    var sum = 0
    for (x <- nums) {
      s.add(x)
      sum += x
    }
    var ans = math.max(1, sum / nums.length + 1)
    while (s.contains(ans)) ans += 1
    ans
  }
}
