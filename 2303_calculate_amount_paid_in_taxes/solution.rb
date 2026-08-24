# LeetCode 2303 - Calculate Amount Paid in Taxes
# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

# @param {Integer[][]} brackets
# @param {Integer} income
# @return {Float}
def calculate_tax(brackets, income)
  ans = 0.0
  prev = 0
  brackets.each do |upper, percent|
    break if income <= prev

    taxable = income < upper ? income - prev : upper - prev
    ans += taxable * percent / 100.0
    prev = upper
  end
  ans
end
