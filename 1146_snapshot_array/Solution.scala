// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

class SnapshotArray(_length: Int) {
  private var snapId = 0
  private val data = Array.fill(_length)(scala.collection.mutable.ArrayBuffer((0, 0)))

  def set(index: Int, `val`: Int): Unit = {
    val hist = data(index)
    if (hist.last._1 == snapId) hist(hist.length - 1) = (snapId, `val`)
    else hist += ((snapId, `val`))
  }

  def snap(): Int = {
    snapId += 1
    snapId - 1
  }

  def get(index: Int, snap_id: Int): Int = {
    val hist = data(index)
    var lo = 0
    var hi = hist.length - 1
    var ans = 0
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (hist(mid)._1 <= snap_id) {
        ans = hist(mid)._2
        lo = mid + 1
      } else hi = mid - 1
    }
    ans
  }
}
