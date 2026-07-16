// LeetCode 0372 - Super Pow

// https://leetcode.com/problems/super-pow/



object Solution {

  def superPow(a: Int, b: Array[Int]): Int = {

    val mod = 1337

    var base = a % mod

    var result = 1



    for (digit <- b) {

      result = (powMod(result, 10, mod).toLong * powMod(base, digit, mod) % mod).toInt

    }



    result

  }



  private def powMod(base: Int, exponent: Int, mod: Int): Int = {

    var currentBase = base.toLong

    var currentExponent = exponent

    var result = 1L



    while (currentExponent > 0) {

      if ((currentExponent & 1) == 1) {

        result = result * currentBase % mod

      }

      currentBase = currentBase * currentBase % mod

      currentExponent >>= 1

    }



    result.toInt

  }

}
