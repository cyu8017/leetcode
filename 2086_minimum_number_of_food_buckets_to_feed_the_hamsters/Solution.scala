// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

object Solution {
  def minimumBuckets(hamsters: String): Int = {
    val b = hamsters.toCharArray
    var ans = 0
    var i = 0
    while (i < b.length) {
      if (b(i) == 'H') {
        if (!(i > 0 && b(i - 1) == 'B')) {
          if (i + 1 < b.length && b(i + 1) == '.') { b(i + 1) = 'B'; ans += 1 }
          else if (i > 0 && b(i - 1) == '.') { b(i - 1) = 'B'; ans += 1 }
          else return -1
        }
      }
      i += 1
    }
    ans
  }
}
