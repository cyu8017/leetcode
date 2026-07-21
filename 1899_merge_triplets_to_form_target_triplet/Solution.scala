// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

object Solution {
  def mergeTriplets(triplets: Array[Array[Int]], target: Array[Int]): Boolean = {
    val merged = Array(0, 0, 0)
    for (t <- triplets) {
      if (t(0) <= target(0) && t(1) <= target(1) && t(2) <= target(2)) {
        merged(0) = math.max(merged(0), t(0))
        merged(1) = math.max(merged(1), t(1))
        merged(2) = math.max(merged(2), t(2))
      }
    }
    merged.sameElements(target)
  }
}
