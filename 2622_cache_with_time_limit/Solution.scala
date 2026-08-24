// LeetCode 2622 - Cache With Time Limit
// https://leetcode.com/problems/cache-with-time-limit/

class TimeLimitedCache() {
  private class Entry(var value: Int, var expire: Long)

  private val data = scala.collection.mutable.HashMap.empty[Int, Entry]
  private val start = System.nanoTime()

  private def nowMs(): Long = (System.nanoTime() - start) / 1000000L

  def set(key: Int, value: Int, duration: Int): Boolean = {
    val now = nowMs()
    val e = data.get(key)
    val alive = e.isDefined && e.get.expire > now
    data(key) = new Entry(value, now + duration)
    alive
  }

  def get(key: Int): Int = {
    val now = nowMs()
    data.get(key) match {
      case Some(e) if e.expire > now => e.value
      case _ => -1
    }
  }

  def count(): Int = {
    val now = nowMs()
    var cnt = 0
    val dead = scala.collection.mutable.ArrayBuffer.empty[Int]
    data.foreach { case (k, e) =>
      if (e.expire > now) cnt += 1
      else dead += k
    }
    dead.foreach(data.remove)
    cnt
  }
}
