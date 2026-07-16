// LeetCode 0455 - Assign Cookies
// https://leetcode.com/problems/assign-cookies/

object Solution {
  def findContentChildren(g: Array[Int], s: Array[Int]): Int = {
    val children = g.sorted
    val cookies = s.sorted
    var child = 0
    var cookie = 0
    while (child < children.length && cookie < cookies.length) {
      if (cookies(cookie) >= children(child)) {
        child += 1
      }
      cookie += 1
    }
    child
  }
}
