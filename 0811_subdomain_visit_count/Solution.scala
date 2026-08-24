// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

object Solution {
  def subdomainVisits(cpdomains: Array[String]): List[String] = {
    val counts = scala.collection.mutable.Map.empty[String, Int]
    cpdomains.foreach { item =>
      val space = item.indexOf(' ')
      val count = item.substring(0, space).toInt
      var domain = item.substring(space + 1)
      var cont = true
      while (cont) {
        counts(domain) = counts.getOrElse(domain, 0) + count
        val dot = domain.indexOf('.')
        if (dot < 0) cont = false
        else domain = domain.substring(dot + 1)
      }
    }
    counts.map { case (k, v) => s"$v $k" }.toList
  }
}
