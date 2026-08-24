// LeetCode 3668 - Restore Finishing Order
// https://leetcode.com/problems/restore-finishing-order/

object Solution {
  def recoverOrder(order: Array[Int], friends: Array[Int]): Array[Int] = {
    val n = order.length
    val d = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      d(order(i)) = i
      i += 1
    }
    val boxed = new Array[Integer](friends.length)
    i = 0
    while (i < friends.length) {
      boxed(i) = friends(i)
      i += 1
    }
    java.util.Arrays.sort(boxed, (a: Integer, b: Integer) => Integer.compare(d(a), d(b)))
    i = 0
    while (i < friends.length) {
      friends(i) = boxed(i)
      i += 1
    }
    friends
  }
}
