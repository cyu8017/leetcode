// LeetCode 1299 - Replace Elements with Greatest Element on Right Side
// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

object Solution {
  def replaceElements(arr: Array[Int]): Array[Int] = {
    var greatest = -1
    for (i <- arr.length - 1 to 0 by -1) {
      val cur = arr(i)
      arr(i) = greatest
      greatest = math.max(greatest, cur)
    }
    arr
  }
}
