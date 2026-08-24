// LeetCode 2890 - Reshape Data: Melt
// https://leetcode.com/problems/reshape-data-melt/

object Solution {
  def meltTable(report: Array[Any]): Array[Map[String, Any]] = {
    report.flatMap {
      case r: Seq[_] =>
        (1 to 4).map { q =>
          Map("product" -> r(0), "quarter" -> s"quarter_$q", "sales" -> r(q))
        }
      case r: Array[_] =>
        (1 to 4).map { q =>
          Map("product" -> r(0), "quarter" -> s"quarter_$q", "sales" -> r(q))
        }
      case r: Map[String, Any] @unchecked =>
        Seq("quarter_1", "quarter_2", "quarter_3", "quarter_4").map { q =>
          Map("product" -> r("product"), "quarter" -> q, "sales" -> r(q))
        }
    }
  }
}
