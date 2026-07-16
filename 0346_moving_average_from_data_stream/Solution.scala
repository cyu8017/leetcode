// LeetCode 0346 - Moving Average from Data Stream

// https://leetcode.com/problems/moving-average-from-data-stream/



import scala.collection.mutable



class MovingAverage(size: Int) {

  private val values = mutable.Queue.empty[Int]

  private var total = 0



  def next(value: Int): Double = {

    values.enqueue(value)

    total += value

    if (values.size > size) {

      total -= values.dequeue()

    }

    total.toDouble / values.size

  }

}
