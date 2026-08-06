object Solution {
  def sumFourDivisors(nums: Array[Int]): Int = nums.map { x => val ds = scala.collection.mutable.Set[Int](); var d = 1; while (d * d <= x && ds.size <= 4) { if (x % d == 0) { ds += d; ds += x / d }; d += 1 }; if (ds.size == 4) ds.sum else 0 }.sum
}
