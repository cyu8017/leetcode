// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

class StatisticsTracker() {
  private val arr = scala.collection.mutable.ArrayBuffer.empty[Int]
  private var sum = 0L
  private val freq = scala.collection.mutable.HashMap.empty[Int, Int]
  private var modeFreq = 0
  private val modes = scala.collection.mutable.HashSet.empty[Int]

  def addNumber(num: Int): Unit = {
    arr += num
    sum += num
    val f = freq.getOrElse(num, 0) + 1
    freq(num) = f
    if (f > modeFreq) {
      modeFreq = f
      modes.clear()
      modes += num
    } else if (f == modeFreq) {
      modes += num
    }
  }

  def removeFirst(): Unit = {
    if (arr.isEmpty) return
    val num = arr.remove(0)
    sum -= num
    val f = freq(num) - 1
    if (f == 0) freq.remove(num)
    else freq(num) = f
    modeFreq = 0
    modes.clear()
    for ((v, ff) <- freq) {
      if (ff > modeFreq) {
        modeFreq = ff
        modes.clear()
        modes += v
      } else if (ff == modeFreq) {
        modes += v
      }
    }
  }

  def getMean(): Int = {
    if (arr.isEmpty) 0
    else (sum / arr.length).toInt
  }

  def getMedian(): Int = {
    val n = arr.length
    val tmp = arr.sorted
    if (n % 2 == 1) tmp(n / 2) else tmp(n / 2 - 1)
  }

  def getMode(): Int = {
    var best = Long.MaxValue
    for (v <- modes) if (v < best) best = v
    if (best == Long.MaxValue) 0 else best.toInt
  }
}
