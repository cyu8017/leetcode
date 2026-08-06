class UndergroundSystem() {
  private val checkIns = scala.collection.mutable.Map[Int, (String, Int)]()
  private val stats = scala.collection.mutable.Map[(String, String), (Long, Long)]().withDefaultValue((0L, 0L))
  def checkIn(id: Int, stationName: String, t: Int): Unit = checkIns(id) = (stationName, t)
  def checkOut(id: Int, stationName: String, t: Int): Unit = { val (start, begin) = checkIns.remove(id).get; val key = (start, stationName); val (total, count) = stats(key); stats(key) = (total + t - begin, count + 1) }
  def getAverageTime(startStation: String, endStation: String): Double = { val (total, count) = stats((startStation, endStation)); total.toDouble / count }
}
