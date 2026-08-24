// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/

object Solution {
  def partial(fn: Array[Int] => Int, args: Array[Int]): Array[Int] => Int = {
    rest => {
      val full = scala.collection.mutable.ArrayBuffer.empty[Int]
      var ri = 0
      args.foreach { a =>
        if (a == Int.MinValue) {
          if (ri < rest.length) {
            full += rest(ri)
            ri += 1
          }
        } else full += a
      }
      while (ri < rest.length) {
        full += rest(ri)
        ri += 1
      }
      fn(full.toArray)
    }
  }
}
