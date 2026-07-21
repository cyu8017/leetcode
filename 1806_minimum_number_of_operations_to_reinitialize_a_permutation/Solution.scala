// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

object Solution {
  def reinitializePermutation(n: Int): Int = {
    var perm = Array.tabulate(n)(identity)
    val target = Array.tabulate(n)(identity)
    var operations = 0
    while (true) {
      val next = Array.ofDim[Int](n)
      for (i <- 0 until n) {
        if (i % 2 == 0) next(i) = perm(i / 2)
        else next(i) = perm(n / 2 + (i - 1) / 2)
      }
      perm = next
      operations += 1
      if (perm.sameElements(target)) return operations
    }
    operations
  }
}
