// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

object Solution {
  def constructDistancedSequence(n: Int): Array[Int] = {
    val ans = Array.fill(2 * n - 1)(0)
    val used = Array.fill(n + 1)(false)

    def backtrack(start: Int): Boolean = {
      var i = start
      while (i < ans.length && ans(i) != 0) {
        i += 1
      }
      if (i == ans.length) {
        return true
      }
      var value = n
      while (value >= 1) {
        if (!used(value)) {
          if (value == 1) {
            ans(i) = 1
            used(1) = true
            if (backtrack(i + 1)) {
              return true
            }
            used(1) = false
            ans(i) = 0
          } else {
            val j = i + value
            if (j < ans.length && ans(j) == 0) {
              ans(i) = value
              ans(j) = value
              used(value) = true
              if (backtrack(i + 1)) {
                return true
              }
              used(value) = false
              ans(i) = 0
              ans(j) = 0
            }
          }
        }
        value -= 1
      }
      false
    }

    backtrack(0)
    ans
  }
}
