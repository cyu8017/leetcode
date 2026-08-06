object Solution {
  def maxNumberOfFamilies(n: Int, reservedSeats: Array[Array[Int]]): Int = {
    val rows = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
    reservedSeats.foreach { s => if (s(1) >= 2 && s(1) <= 9) rows(s(0)) = rows(s(0)) | (1 << (s(1) - 2)) }
    2 * (n - rows.size) + rows.values.map { x => val l = (x & 15) == 0; val r = (x & 240) == 0; val m = (x & 60) == 0; if (l && r) 2 else if (l || r || m) 1 else 0 }.sum
  }
}
