# LeetCode 2806 - Account Balance After Rounded Purchase
# https://leetcode.com/problems/account-balance-after-rounded-purchase/

# @param {Integer} purchase_amount
# @return {Integer}
def account_balance_after_purchase(purchase_amount)
  r = ((purchase_amount + 5) / 10) * 10
  100 - r
end
