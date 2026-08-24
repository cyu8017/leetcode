// LeetCode 0904 - Fruit Into Baskets
// https://leetcode.com/problems/fruit-into-baskets/

object Solution {
  def totalFruit(fruits: Array[Int]): Int = {
    val count = scala.collection.mutable.Map.empty[Int, Int]
    var left = 0
    var ans = 0
    var right = 0
    while (right < fruits.length) {
      count(fruits(right)) = count.getOrElse(fruits(right), 0) + 1
      while (count.size > 2) {
        val c = count(fruits(left)) - 1
        if (c == 0) count.remove(fruits(left))
        else count(fruits(left)) = c
        left += 1
      }
      ans = math.max(ans, right - left + 1)
      right += 1
    }
    ans
  }
}
