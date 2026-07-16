// LeetCode 0371 - Sum of Two Integers

// https://leetcode.com/problems/sum-of-two-integers/



object Solution {

  def getSum(a: Int, b: Int): Int = {

    var x = a

    var y = b

    val mask = 0xFFFFFFFF



    while (y != 0) {

      val carry = (x & y) << 1

      x = (x ^ y) & mask

      y = carry & mask

    }



    if (x <= 0x7FFFFFFF) x else ~(x ^ mask)

  }

}
