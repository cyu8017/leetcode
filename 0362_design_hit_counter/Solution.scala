// LeetCode 0362 - Design Hit Counter

// https://leetcode.com/problems/design-hit-counter/



import scala.collection.mutable



class HitCounter {

  private val hits = mutable.Queue.empty[Int]



  def hit(timestamp: Int): Unit = {

    hits.enqueue(timestamp)

  }



  def getHits(timestamp: Int): Int = {

    while (hits.nonEmpty && hits.head <= timestamp - 300) {

      hits.dequeue()

    }

    hits.size

  }

}
