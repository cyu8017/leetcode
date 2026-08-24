// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/

object Solution {
  def compose(functions: List[Int => Int]): Int => Int = {
    (x0: Int) => {
      var x = x0
      var i = functions.length - 1
      while (i >= 0) {
        x = functions(i)(x)
        i -= 1
      }
      x
    }
  }
}
