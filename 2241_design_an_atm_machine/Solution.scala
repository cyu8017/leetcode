// LeetCode 2241 - Design an ATM Machine
// https://leetcode.com/problems/design-an-atm-machine/

class ATM() {
  private val cnt = Array.fill(5)(0L)
  private val vals = Array(20, 50, 100, 200, 500)

  def deposit(banknotesCount: Array[Int]): Unit = {
    var i = 0
    while (i < 5) {
      cnt(i) += banknotesCount(i)
      i += 1
    }
  }

  def withdraw(amount: Int): Array[Int] = {
    val take = new Array[Int](5)
    var remain = amount.toLong
    val tmp = cnt.clone()
    var i = 4
    while (i >= 0) {
      var need = remain / vals(i)
      if (need > tmp(i)) need = tmp(i)
      take(i) = need.toInt
      remain -= need * vals(i)
      i -= 1
    }
    if (remain != 0) return Array(-1)
    i = 0
    while (i < 5) {
      cnt(i) -= take(i)
      i += 1
    }
    take
  }
}
