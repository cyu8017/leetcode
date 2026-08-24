// LeetCode 2887 - Fill Missing Data
// https://leetcode.com/problems/fill-missing-data/

object Solution {
  def fillMissingValues(products: Array[Any]): Array[Any] = {
    products.map {
      case r: Seq[_] => Seq(r(0), if (r(1) == null) 0 else r(1), r(2))
      case r: Array[_] => Array(r(0), if (r(1) == null) 0 else r(1), r(2))
      case r: Map[String, Any] @unchecked =>
        r + ("quantity" -> (if (r.getOrElse("quantity", null) == null) 0 else r("quantity")))
    }
  }
}
