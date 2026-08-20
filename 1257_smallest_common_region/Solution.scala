// LeetCode 1257 - Smallest Common Region
// https://leetcode.com/problems/smallest-common-region/

object Solution {
  def findSmallestRegion(regions: List[List[String]], region1: String, region2: String): String = {
    val parent = scala.collection.mutable.Map.empty[String, String]
    for (group <- regions; child <- group.tail) parent(child) = group.head
    val ancestors = scala.collection.mutable.Set.empty[String]
    var r1: String = region1
    while (r1 != null) {
      ancestors += r1
      r1 = parent.getOrElse(r1, null)
    }
    var r2 = region2
    while (!ancestors.contains(r2)) r2 = parent(r2)
    r2
  }
}
