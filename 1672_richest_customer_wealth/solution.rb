# LeetCode 1672 - Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/

# @param {Integer[][]} accounts
# @return {Integer}
def maximum_wealth(accounts)
  accounts.map(&:sum).max
end
