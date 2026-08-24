// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

object Solution {
  def minSwaps(nums: Array[Int], forbidden: Array[Int]): Int = {
    val n = nums.length
    val freq = new java.util.HashMap[Integer, Integer]()
    nums.foreach { x =>
      if (!freq.containsKey(x)) freq.put(x, 0)
      freq.merge(x, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }
    forbidden.foreach { x =>
      if (!freq.containsKey(x)) freq.put(x, 0)
      freq.merge(x, 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
    }
    val it = freq.values().iterator()
    while (it.hasNext) {
      if (it.next() > n) return -1
    }
    val bad = new java.util.HashMap[Integer, Integer]()
    var total = 0
    var largest = 0
    var i = 0
    while (i < n) {
      if (nums(i) == forbidden(i)) {
        if (!bad.containsKey(nums(i))) bad.put(nums(i), 0)
        bad.merge(nums(i), 1, (a: Integer, b: Integer) => Integer.valueOf(a + b))
        total += 1
        if (bad.get(nums(i)) > largest) largest = bad.get(nums(i))
      }
      i += 1
    }
    if ((total + 1) / 2 > largest) (total + 1) / 2 else largest
  }
}
