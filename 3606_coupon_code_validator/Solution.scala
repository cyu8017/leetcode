// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

object Solution {
  def check(s: String): Boolean = {
    if (s.isEmpty) return false
    for (c <- s.toCharArray)
      if (!Character.isLetterOrDigit(c) && c != '_') return false
    true
  }

  def validateCoupons(code: Array[String], businessLine: Array[String], isActive: Array[Boolean]): java.util.List[String] = {
    val bs = new java.util.HashSet[String]()
    java.util.Collections.addAll(bs, "electronics", "grocery", "pharmacy", "restaurant")
    val idx = new java.util.ArrayList[Integer]()
    var i = 0
    while (i < code.length) {
      if (isActive(i) && bs.contains(businessLine(i)) && check(code(i))) idx.add(i)
      i += 1
    }
    idx.sort((a: Integer, b: Integer) => {
      val c = businessLine(a).compareTo(businessLine(b))
      if (c != 0) c else code(a).compareTo(code(b))
    })
    val ans = new java.util.ArrayList[String]()
    val it = idx.iterator()
    while (it.hasNext) ans.add(code(it.next()))
    ans
  }
}
