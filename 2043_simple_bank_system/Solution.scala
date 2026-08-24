// LeetCode 2043 - Simple Bank System
// https://leetcode.com/problems/simple-bank-system/

class Bank(_balance: Array[Long]) {
  private val bal = _balance.clone()

  private def valid(account: Int): Boolean = account >= 1 && account <= bal.length

  def transfer(account1: Int, account2: Int, money: Long): Boolean = {
    if (!valid(account1) || !valid(account2) || bal(account1 - 1) < money) false
    else {
      bal(account1 - 1) -= money
      bal(account2 - 1) += money
      true
    }
  }

  def deposit(account: Int, money: Long): Boolean = {
    if (!valid(account)) false
    else { bal(account - 1) += money; true }
  }

  def withdraw(account: Int, money: Long): Boolean = {
    if (!valid(account) || bal(account - 1) < money) false
    else { bal(account - 1) -= money; true }
  }
}
