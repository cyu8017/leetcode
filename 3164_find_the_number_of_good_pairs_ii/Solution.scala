// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

object Solution {
  def numberOfPairs(nums1: Array[Int], nums2: Array[Int], k: Int): Long = {
    val cnt1 = scala.collection.mutable.Map.empty[Int, Int]
    nums1.foreach { x =>
      if (x % k == 0) cnt1(x / k) = cnt1.getOrElse(x / k, 0) + 1
    }
    if (cnt1.isEmpty) return 0
    val cnt2 = scala.collection.mutable.Map.empty[Int, Int]
    nums2.foreach(x => cnt2(x) = cnt2.getOrElse(x, 0) + 1)
    var mx = 0
    cnt1.keys.foreach(x => mx = math.max(mx, x))
    var ans = 0L
    cnt2.foreach { case (x, v) =>
      var s = 0
      var y = x
      while (y <= mx) {
        cnt1.get(y).foreach(c => s += c)
        y += x
      }
      ans += s.toLong * v
    }
    ans
  }
}
