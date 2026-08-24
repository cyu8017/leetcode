// LeetCode 0630 - Course Schedule III
// https://leetcode.com/problems/course-schedule-iii/

import scala.collection.mutable

object Solution {
  def scheduleCourse(courses: Array[Array[Int]]): Int = {
    val sorted = courses.sortBy(_(1))
    val heap = mutable.PriorityQueue.empty[Int]
    var time = 0
    sorted.foreach { course =>
      val duration = course(0)
      val lastDay = course(1)
      if (time + duration <= lastDay) {
        heap.enqueue(duration)
        time += duration
      } else if (heap.nonEmpty && heap.head > duration) {
        time += duration - heap.dequeue()
        heap.enqueue(duration)
      }
    }
    heap.size
  }
}
