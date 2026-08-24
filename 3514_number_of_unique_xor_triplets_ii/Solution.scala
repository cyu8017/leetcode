// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

object Solution {
  def uniqueXorTriplets(nums: Array[Int]): Int = {
    var mx = 0
    for (v <- nums) mx = math.max(mx, v)
    mx <<= 1
    val st = new Array[Boolean](mx)
    for (a <- nums; b <- nums) st(a ^ b) = true
    val s = new Array[Int](mx)
    var ab = 0
    while (ab < mx) {
      if (st(ab)) for (c <- nums) s(ab ^ c) = 1
      ab += 1
    }
    var ans = 0
    for (v <- s) ans += v
    ans
  }
}
