# LeetCode 0860 - Lemonade Change
# https://leetcode.com/problems/lemonade-change/

# @param {Integer[]} bills
# @return {Boolean}
def lemonade_change(bills)
  fives = 0
  tens = 0
  bills.each do |bill|
    if bill == 5
      fives += 1
    elsif bill == 10
      return false if fives.zero?

      fives -= 1
      tens += 1
    elsif tens.positive? && fives.positive?
      tens -= 1
      fives -= 1
    elsif fives >= 3
      fives -= 3
    else
      return false
    end
  end
  true
end
