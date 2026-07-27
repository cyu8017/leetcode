// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

object Solution {
  def maximumRequests(n: Int, requests: Array[Array[Int]]): Int = {
    val m = requests.length
    var ans = 0
    var mask = 0
    while (mask < (1 << m)) {
      val cnt = Integer.bitCount(mask)
      if (cnt > ans) {
        val bal = Array.fill(n)(0)
        var i = 0
        while (i < m) {
          if (((mask >> i) & 1) == 1) {
            bal(requests(i)(0)) -= 1
            bal(requests(i)(1)) += 1
          }
          i += 1
        }
        if (bal.forall(_ == 0)) ans = cnt
      }
      mask += 1
    }
    ans
  }
}
