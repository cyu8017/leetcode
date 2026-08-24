// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

object Solution {
  def maxWeight(pizzas: Array[Int]): Long = {
    java.util.Arrays.sort(pizzas)
    val n = pizzas.length
    val days = n / 4
    var ans = 0L
    val oddDays = (days + 1) / 2
    val evenDays = days / 2
    var idx = n - 1
    var i = 0
    while (i < oddDays) {
      ans += pizzas(idx)
      idx -= 1
      i += 1
    }
    i = 0
    while (i < evenDays) {
      idx -= 1
      ans += pizzas(idx)
      idx -= 1
      i += 1
    }
    ans
  }
}
