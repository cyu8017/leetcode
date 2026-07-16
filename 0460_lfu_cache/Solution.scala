// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

import scala.collection.mutable

class LFUCache(capacity: Int) {
  private var minFreq = 0
  private val keyValues = mutable.Map.empty[Int, Int]
  private val keyFreqs = mutable.Map.empty[Int, Int]
  private val freqKeys = mutable.Map.empty[Int, mutable.ArrayBuffer[Int]].withDefaultValue(
    mutable.ArrayBuffer.empty[Int]
  )

  private def touch(key: Int): Unit = {
    val freq = keyFreqs(key)
    val bucket = freqKeys(freq)
    bucket -= key
    if (bucket.isEmpty && freq == minFreq) {
      minFreq += 1
    }
    keyFreqs(key) = freq + 1
    freqKeys(freq + 1) += key
  }

  def get(key: Int): Int = {
    if (!keyValues.contains(key)) return -1
    touch(key)
    keyValues(key)
  }

  def put(key: Int, value: Int): Unit = {
    if (capacity == 0) return
    if (keyValues.contains(key)) {
      keyValues(key) = value
      touch(key)
      return
    }

    if (keyValues.size >= capacity) {
      val evict = freqKeys(minFreq).remove(0)
      keyValues -= evict
      keyFreqs -= evict
    }

    keyValues(key) = value
    keyFreqs(key) = 1
    freqKeys(1) += key
    minFreq = 1
  }
}
