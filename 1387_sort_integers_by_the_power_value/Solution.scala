object Solution {
  private val memo = scala.collection.mutable.Map[Int, Int](1 -> 0)
  private def power(x: Int): Int = memo.getOrElseUpdate(x, 1 + power(if (x % 2 == 0) x / 2 else 3 * x + 1))
  def getKth(lo: Int, hi: Int, k: Int): Int = (lo to hi).sortBy(x => (power(x), x))(k - 1)
}
