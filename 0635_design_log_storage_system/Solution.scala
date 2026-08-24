// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

import scala.collection.mutable

class LogSystem() {
  private val ids = mutable.ArrayBuffer.empty[Int]
  private val timestamps = mutable.ArrayBuffer.empty[String]
  private val granularityIndex = mutable.Map(
    "Year" -> 4,
    "Month" -> 7,
    "Day" -> 10,
    "Hour" -> 13,
    "Minute" -> 16,
    "Second" -> 19,
  )

  def put(id: Int, timestamp: String): Unit = {
    ids += id
    timestamps += timestamp
  }

  def retrieve(start: String, end: String, granularity: String): List[Int] = {
    val index = granularityIndex(granularity)
    val startKey = start.substring(0, index)
    val endKey = end.substring(0, index)
    val matched = mutable.ArrayBuffer.empty[(String, Int)]
    var i = 0
    while (i < timestamps.size) {
      val timestamp = timestamps(i)
      val key = timestamp.substring(0, index)
      if (startKey.compareTo(key) <= 0 && key.compareTo(endKey) <= 0) {
        matched += ((timestamp, ids(i)))
      }
      i += 1
    }
    matched.sortBy(_._1).map(_._2).toList
  }
}
