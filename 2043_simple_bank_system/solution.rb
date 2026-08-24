# LeetCode 2043 - Simple Bank System
# https://leetcode.com/problems/simple-bank-system/

class Bank
  def initialize(balance)
    @bal = balance.dup
  end

  def transfer(account1, account2, money)
    return false unless valid(account1) && valid(account2) && @bal[account1 - 1] >= money

    @bal[account1 - 1] -= money
    @bal[account2 - 1] += money
    true
  end

  def deposit(account, money)
    return false unless valid(account)

    @bal[account - 1] += money
    true
  end

  def withdraw(account, money)
    return false unless valid(account) && @bal[account - 1] >= money

    @bal[account - 1] -= money
    true
  end

  private

  def valid(account)
    account >= 1 && account <= @bal.length
  end
end
