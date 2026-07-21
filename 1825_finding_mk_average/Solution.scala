// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

import scala.collection.mutable

class MKAverage(_m: Int, _k: Int) {
  private val m = _m
  private val k = _k
  private val stream = mutable.ArrayBuffer.empty[Int]

  def addElement(num: Int): Unit = {
    stream += num
  }

  def calculateMKAverage(): Int = {
    if (stream.size < m) return -1
    val window = stream.takeRight(m).sorted
    val middle = window.slice(k, window.length - k)
    middle.sum / middle.length
  }
}
