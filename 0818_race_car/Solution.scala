// LeetCode 0818 - Race Car
// https://leetcode.com/problems/race-car/

object Solution {
  def racecar(target: Int): Int = {
    def key(pos: Int, speed: Int): Long = (pos.toLong << 20) ^ (speed & 0xfffffL)
    val queue = scala.collection.mutable.Queue[(Int, Int, Int)]((0, 1, 0))
    val seen = scala.collection.mutable.Set(key(0, 1))
    while (queue.nonEmpty) {
      val (pos, speed, steps) = queue.dequeue()
      if (pos == target) return steps
      val nxtPos = pos + speed
      val nxtSpeed = speed * 2
      if (!seen.contains(key(nxtPos, nxtSpeed)) && math.abs(nxtPos) < target * 2) {
        seen += key(nxtPos, nxtSpeed)
        queue.enqueue((nxtPos, nxtSpeed, steps + 1))
      }
      val revSpeed = if (speed > 0) -1 else 1
      if (seen.add(key(pos, revSpeed))) queue.enqueue((pos, revSpeed, steps + 1))
    }
    -1
  }
}
