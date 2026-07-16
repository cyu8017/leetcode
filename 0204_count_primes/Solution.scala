// LeetCode 0204 - Count Primes\n// https://leetcode.com/problems/\n\nobject Solution {
  def countPrimes(n: Int): Int = {
    if (n <= 2) return 0
    val prime = Array.fill(n)(true)
    var p = 2
    while (p * p < n) {
      if (prime(p)) { var multiple = p * p; while (multiple < n) { prime(multiple) = false; multiple += p } }
      p += 1
    }
    (2 until n).count(prime)
  }
}
