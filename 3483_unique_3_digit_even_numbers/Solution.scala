// LeetCode 3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/

object Solution {
  def totalNumbers(digits: Array[Int]): Int = {
    val seen = scala.collection.mutable.Set.empty[Int]
    val n = digits.length
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (j != i) {
          var k = 0
          while (k < n) {
            if (k != i && k != j && digits(i) != 0 && digits(k) % 2 == 0) {
              seen += digits(i) * 100 + digits(j) * 10 + digits(k)
            }
            k += 1
          }
        }
        j += 1
      }
      i += 1
    }
    seen.size
  }
}
