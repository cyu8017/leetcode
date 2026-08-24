// LeetCode 2889 - Reshape Data: Pivot
// https://leetcode.com/problems/reshape-data-pivot/

object Solution {
  def pivotTable(weather: Array[Any]): Array[Map[String, Any]] = {
    val months = scala.collection.mutable.ArrayBuffer.empty[Any]
    val byMonth = scala.collection.mutable.LinkedHashMap.empty[Any, scala.collection.mutable.Map[Any, Any]]
    weather.foreach {
      case r: Seq[_] => add(months, byMonth, r(0), r(1), r(2))
      case r: Array[_] => add(months, byMonth, r(0), r(1), r(2))
      case r: Map[String, Any] @unchecked =>
        add(months, byMonth, r("city"), r("month"), r("temperature"))
    }
    months.map { month =>
      Map[String, Any]("month" -> month) ++ byMonth(month).map { case (k, v) => k.toString -> v }
    }.toArray
  }

  private def add(
      months: scala.collection.mutable.ArrayBuffer[Any],
      byMonth: scala.collection.mutable.LinkedHashMap[Any, scala.collection.mutable.Map[Any, Any]],
      city: Any,
      month: Any,
      temperature: Any
  ): Unit = {
    if (!byMonth.contains(month)) {
      byMonth(month) = scala.collection.mutable.Map.empty[Any, Any]
      months += month
    }
    byMonth(month)(city) = temperature
  }
}
