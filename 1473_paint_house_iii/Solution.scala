object Solution {
  def minCost(houses: Array[Int], cost: Array[Array[Int]], m: Int, n: Int, target: Int): Int = {
    val inf = Long.MaxValue / 4
    var dp = Map((0, 0) -> 0L)
    for (i <- houses.indices) {
      var next = Map.empty[(Int, Int), Long]
      val colors = if (houses(i) == 0) 1 to n else Seq(houses(i))
      for (((previous, groups), value) <- dp; color <- colors) {
        val newGroups = groups + (if (color != previous) 1 else 0)
        if (newGroups <= target) {
          val candidate = value + (if (houses(i) == 0) cost(i)(color - 1).toLong else 0L)
          val key = (color, newGroups)
          next = next.updated(key, math.min(next.getOrElse(key, inf), candidate))
        }
      }
      dp = next
    }
    val answer = dp.collect { case ((_, groups), value) if groups == target => value }.minOption.getOrElse(inf)
    if (answer == inf) -1 else answer.toInt
  }
}
