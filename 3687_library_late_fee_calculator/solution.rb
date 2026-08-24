# LeetCode 3687 - Library Late Fee Calculator
# https://leetcode.com/problems/library-late-fee-calculator/

# @param {Integer[]} days_late
# @return {Integer}
def late_fee(days_late)
  fee = lambda do |x|
    return 1 if x == 1
    return 3 * x if x > 5

    2 * x
  end
  days_late.sum { |x| fee.call(x) }
end
