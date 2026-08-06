object Solution {
  def avoidFlood(rains: Array[Int]): Array[Int] = {
    val answer = Array.fill(rains.length)(-1)
    val full = scala.collection.mutable.HashMap.empty[Int, Int]
    val dry = new java.util.TreeSet[Int]()
    for (day <- rains.indices) {
      val lake = rains(day)
      if (lake == 0) {
        dry.add(day)
        answer(day) = 1
      } else {
        full.get(lake).foreach { previous =>
          val dryDay = dry.higher(previous)
          if (dryDay == null) return Array.emptyIntArray
          answer(dryDay) = lake
          dry.remove(dryDay)
        }
        full(lake) = day
      }
    }
    answer
  }
}
