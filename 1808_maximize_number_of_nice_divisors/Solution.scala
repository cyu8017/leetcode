// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

object Solution {
  def maxNiceDivisors(primeFactors: Int): Int = {
    val MOD = BigInt(1000000007)
    if (primeFactors <= 3) return primeFactors
    if (primeFactors % 3 == 0) BigInt(3).modPow(primeFactors / 3, MOD).toInt
    else if (primeFactors % 3 == 1)
      ((BigInt(3).modPow(primeFactors / 3 - 1, MOD) * 4) % MOD).toInt
    else
      ((BigInt(3).modPow(primeFactors / 3, MOD) * 2) % MOD).toInt
  }
}
