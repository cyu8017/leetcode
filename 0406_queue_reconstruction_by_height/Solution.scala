// LeetCode 0406 - Queue Reconstruction by Height

// https://leetcode.com/problems/queue-reconstruction-by-height/



import scala.collection.mutable



object Solution {

  def reconstructQueue(people: Array[Array[Int]]): Array[Array[Int]] = {

    val sorted = people.sortWith((a, b) =>

      if (a(0) != b(0)) a(0) > b(0) else a(1) < b(1),

    )

    val queue = mutable.ArrayBuffer.empty[Array[Int]]



    for (person <- sorted) {

      queue.insert(person(1), person)

    }



    queue.toArray

  }

}
