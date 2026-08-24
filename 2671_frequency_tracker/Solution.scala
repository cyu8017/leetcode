// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker() {
  private val freq = scala.collection.mutable.HashMap.empty[Int, Int]
  private val count = scala.collection.mutable.HashMap.empty[Int, Int]

  def add(number: Int): Unit = {
    val old = freq.getOrElse(number, 0)
    if (old > 0) count(old) = count.getOrElse(old, 0) - 1
    freq(number) = old + 1
    count(old + 1) = count.getOrElse(old + 1, 0) + 1
  }

  def deleteOne(number: Int): Unit = {
    val old = freq.getOrElse(number, 0)
    if (old == 0) return
    count(old) = count.getOrElse(old, 0) - 1
    freq(number) = old - 1
    if (old - 1 > 0) count(old - 1) = count.getOrElse(old - 1, 0) + 1
  }

  def hasFrequency(frequency: Int): Boolean =
    count.getOrElse(frequency, 0) > 0
}
