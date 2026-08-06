object Solution {
  def findLeastNumOfUniqueInts(arr: Array[Int], k: Int): Int = {
    val counts = arr.groupMapReduce(identity)(_ => 1)(_ + _).values.toSeq.sorted
    var remaining = k
    var removed = 0
    for (count <- counts if remaining >= count) {
      remaining -= count
      removed += 1
    }
    counts.length - removed
  }
}
