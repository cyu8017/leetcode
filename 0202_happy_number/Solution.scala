// LeetCode 0202 - Happy Number\n// https://leetcode.com/problems/\n\nimport scala.collection.mutable

object Solution {
  def isHappy(n: Int): Boolean = {
    val seen = mutable.Set[Int]()
    var value = n
    while (value != 1 && seen.add(value)) value = nextValue(value)
    value == 1
  }

  private def nextValue(value: Int): Int = {
    var number = value
    var total = 0
    while (number > 0) { val digit = number % 10; total += digit * digit; number /= 10 }
    total
  }
}
