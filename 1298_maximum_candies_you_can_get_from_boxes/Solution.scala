// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

object Solution {
  def maxCandies(
    status: Array[Int],
    candies: Array[Int],
    keys: Array[Array[Int]],
    containedBoxes: Array[Array[Int]],
    initialBoxes: Array[Int]
  ): Int = {
    val owned = scala.collection.mutable.Set(initialBoxes: _*)
    val opened = scala.collection.mutable.Set.empty[Int]
    val q = scala.collection.mutable.Queue[Int]()
    for (box <- initialBoxes if status(box) == 1) q.enqueue(box)
    var total = 0
    while (q.nonEmpty) {
      val box = q.dequeue()
      if (!opened.contains(box) && status(box) == 1) {
        opened += box
        total += candies(box)
        for (key <- keys(box)) {
          status(key) = 1
          if (owned.contains(key) && !opened.contains(key)) q.enqueue(key)
        }
        for (child <- containedBoxes(box)) {
          owned += child
          if (status(child) == 1 && !opened.contains(child)) q.enqueue(child)
        }
      }
    }
    total
  }
}
