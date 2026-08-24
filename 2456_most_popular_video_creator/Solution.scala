// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

object Solution {
  private class Info(var total: Long, var bestID: String, var bestViews: Int)

  def mostPopularCreator(creators: Array[String], ids: Array[String], views: Array[Int]): List[List[String]] = {
    val mp = scala.collection.mutable.LinkedHashMap.empty[String, Info]
    var maxTotal = 0L
    var i = 0
    while (i < creators.length) {
      mp.get(creators(i)) match {
        case None =>
          mp(creators(i)) = new Info(views(i).toLong, ids(i), views(i))
        case Some(info) =>
          info.total += views(i)
          if (views(i) > info.bestViews || (views(i) == info.bestViews && ids(i) < info.bestID)) {
            info.bestViews = views(i)
            info.bestID = ids(i)
          }
      }
      val t = mp(creators(i)).total
      if (t > maxTotal) maxTotal = t
      i += 1
    }
    val ans = scala.collection.mutable.ListBuffer.empty[List[String]]
    mp.foreach { case (name, info) =>
      if (info.total == maxTotal) ans += List(name, info.bestID)
    }
    ans.toList
  }
}
