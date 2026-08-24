// LeetCode 3491 - Phone Number Prefix
// https://leetcode.com/problems/phone-number-prefix/

object Solution {
  def phonePrefix(numbers: Array[String]): Boolean = {
    scala.util.Sorting.quickSort(numbers)
    var i = 0
    while (i + 1 < numbers.length) {
      if (numbers(i).length <= numbers(i + 1).length && numbers(i + 1).startsWith(numbers(i)))
        return false
      i += 1
    }
    true
  }
}
