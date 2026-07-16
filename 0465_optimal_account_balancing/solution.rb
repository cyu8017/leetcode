# LeetCode 0465 - Optimal Account Balancing
# https://leetcode.com/problems/optimal-account-balancing/

class Solution
  def min_transfers(transactions)
    balances = Hash.new(0)
    transactions.each do |source, target, amount|
      balances[source] -= amount
      balances[target] += amount
    end

    debts = balances.values.reject(&:zero?)
    dfs(debts, 0)
  end

  alias_method :minTransfers, :min_transfers

  private

  def dfs(debts, index)
    index += 1 while index < debts.length && debts[index].zero?
    return 0 if index == debts.length

    best = debts.length
    ((index + 1)...debts.length).each do |next_index|
      next unless debts[index] * debts[next_index] < 0

      debts[next_index] += debts[index]
      best = [best, 1 + dfs(debts, index + 1)].min
      debts[next_index] -= debts[index]
    end
    best
  end
end
