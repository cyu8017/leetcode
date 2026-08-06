object Solution {
  def findTheDistanceValue(arr1: Array[Int], arr2: Array[Int], d: Int): Int = {
    val b = arr2.sorted
    arr1.count { x => val i = java.util.Arrays.binarySearch(b, x); val p = if (i < 0) -i - 1 else i; !((p < b.length && math.abs(b(p) - x) <= d) || (p > 0 && math.abs(b(p - 1) - x) <= d)) }
  }
}
