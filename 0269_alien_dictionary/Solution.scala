// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

import scala.collection.mutable

object Solution {
  def alienOrder(words: Array[String]): String = {
    val graph = mutable.Map.empty[Char, mutable.Set[Char]].withDefaultValue(mutable.Set.empty[Char])
    val indegree = mutable.Map.empty[Char, Int].withDefaultValue(0)

    words.foreach { word =>
      word.foreach { char =>
        graph.getOrElseUpdate(char, mutable.Set.empty[Char])
        indegree.getOrElseUpdate(char, 0)
      }
    }

    var index = 0
    while (index < words.length - 1) {
      val first = words(index)
      val second = words(index + 1)
      if (first.length > second.length && first.startsWith(second)) {
        return ""
      }
      val limit = math.min(first.length, second.length)
      var j = 0
      while (j < limit) {
        val left = first(j)
        val right = second(j)
        if (left != right) {
          if (!graph(left).contains(right)) {
            graph(left).add(right)
            indegree(right) = indegree(right) + 1
          }
          j = limit
        }
        j += 1
      }
      index += 1
    }

    val queue = mutable.Queue.empty[Char]
    indegree.foreach { case (char, degree) =>
      if (degree == 0) {
        queue.enqueue(char)
      }
    }

    val order = new StringBuilder
    while (queue.nonEmpty) {
      val char = queue.dequeue()
      order.append(char)
      graph(char).foreach { next =>
        indegree(next) = indegree(next) - 1
        if (indegree(next) == 0) {
          queue.enqueue(next)
        }
      }
    }

    if (order.length == indegree.size) order.toString else ""
  }
}
