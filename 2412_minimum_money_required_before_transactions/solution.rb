# LeetCode 2412 - Minimum Money Required Before Transactions
# https://leetcode.com/problems/minimum-money-required-before-transactions/

# @param {Integer[][]} transactions
# @return {Integer}
def minimum_money(transactions)
  total_loss = 0
  max_cashback = 0
  max_cost = 0
  transactions.each do |cost, cashback|
    if cost > cashback
      total_loss += cost - cashback
      max_cashback = cashback if cashback > max_cashback
    elsif cost > max_cost
      max_cost = cost
    end
  end
  [total_loss + max_cashback, total_loss + max_cost].max
end
