import scala.collection.mutable

object Solution {
  def maxStudents(seats: Array[Array[Char]]): Int = {
    val cols = seats.head.length
    var dp = Map(0 -> 0)
    for (row <- seats) {
      val available = row.indices.filter(row(_) == '.').foldLeft(0)((mask, c) => mask | (1 << c))
      val valid = (0 until (1 << cols)).filter(mask => (mask & ~available) == 0 && (mask & (mask << 1)) == 0)
      dp = valid.flatMap(mask => dp.collect {
        case (previous, count) if (mask & (previous << 1)) == 0 && (mask & (previous >> 1)) == 0 => mask -> (count + Integer.bitCount(mask))
      }).groupMapReduce(_._1)(_._2)(math.max)
    }
    dp.values.max
  }
}
