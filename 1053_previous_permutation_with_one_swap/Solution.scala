// LeetCode 1053 - Previous Permutation With One Swap
// https://leetcode.com/problems/previous-permutation-with-one-swap/

object Solution {
  def prevPermOpt1(arr: Array[Int]): Array[Int] = {
    val n = arr.length
    var i = n - 2
    while (i >= 0 && arr(i) <= arr(i + 1)) i -= 1
    if (i < 0) return arr
    var j = n - 1
    while (arr(j) >= arr(i) || arr(j) == arr(j - 1)) j -= 1
    val tmp = arr(i); arr(i) = arr(j); arr(j) = tmp
    arr
  }
}
