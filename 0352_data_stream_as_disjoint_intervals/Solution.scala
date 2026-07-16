// LeetCode 0352 - Data Stream as Disjoint Intervals

// https://leetcode.com/problems/data-stream-as-disjoint-intervals/



import scala.collection.mutable



class SummaryRanges {

  private val intervals = mutable.ArrayBuffer.empty[Array[Int]]



  def addNum(value: Int): Unit = {

    val newInterval = Array(value, value)

    val merged = mutable.ArrayBuffer.empty[Array[Int]]

    var inserted = false



    for (interval <- intervals) {

      if (interval(1) < value - 1) {

        merged += interval

      } else if (interval(0) > value + 1) {

        if (!inserted) {

          merged += newInterval

          inserted = true

        }

        merged += interval

      } else {

        newInterval(0) = math.min(newInterval(0), interval(0))

        newInterval(1) = math.max(newInterval(1), interval(1))

      }

    }



    if (!inserted) {

      merged += newInterval

    }



    intervals.clear()

    intervals ++= merged

  }



  def getIntervals(): Array[Array[Int]] = intervals.toArray

}
