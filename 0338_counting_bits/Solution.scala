// LeetCode 0338 - Counting Bits

// https://leetcode.com/problems/counting-bits/



object Solution {

  def countBits(n: Int): Array[Int] = {

    val result = new Array[Int](n + 1)

    for (index <- 1 to n) {

      result(index) = result(index & (index - 1)) + 1

    }

    result

  }

}
