// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

import scala.collection.mutable

object Solution {
  def alertNames(keyName: Array[String], keyTime: Array[String]): List[String] = {
    val times = mutable.Map.empty[String, mutable.ArrayBuffer[Int]]
    keyName.indices.foreach { i =>
      val parts = keyTime(i).split(":")
      val mins = parts(0).toInt * 60 + parts(1).toInt
      times.getOrElseUpdate(keyName(i), mutable.ArrayBuffer.empty) += mins
    }
    times.iterator.collect {
      case (name, buf) =>
        val a = buf.sorted
        if (a.indices.exists(i => i + 2 < a.length && a(i + 2) - a(i) <= 60)) Some(name)
        else None
    }.flatten.toList.sorted
  }
}
