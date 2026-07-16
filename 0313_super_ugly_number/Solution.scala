// LeetCode 0313 - Super Ugly Number

// https://leetcode.com/problems/super-ugly-number/



object Solution {

  def nthSuperUglyNumber(n: Int, primes: Array[Int]): Int = {

    val ugly = new Array[Int](n)

    ugly(0) = 1

    val pointers = new Array[Int](primes.length)

    for (count <- 1 until n) {

      var nextUgly = Int.MaxValue

      for (index <- primes.indices) {

        nextUgly = math.min(nextUgly, ugly(pointers(index)) * primes(index))

      }

      ugly(count) = nextUgly

      for (index <- primes.indices if nextUgly == ugly(pointers(index)) * primes(index)) {

        pointers(index) += 1

      }

    }

    ugly(n - 1)

  }

}

