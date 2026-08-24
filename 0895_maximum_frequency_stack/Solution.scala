// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack() {
  private val freq = scala.collection.mutable.Map.empty[Int, Int]
  private val group = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
  private var maxfreq = 0

  def push(`val`: Int): Unit = {
    val f = freq.getOrElse(`val`, 0) + 1
    freq(`val`) = f
    maxfreq = math.max(maxfreq, f)
    group.getOrElseUpdate(f, scala.collection.mutable.ArrayBuffer.empty[Int]) += `val`
  }

  def pop(): Int = {
    val list = group(maxfreq)
    val v = list.remove(list.length - 1)
    freq(v) = freq(v) - 1
    if (list.isEmpty) maxfreq -= 1
    v
  }
}
