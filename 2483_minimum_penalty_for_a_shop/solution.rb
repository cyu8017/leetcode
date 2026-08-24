# LeetCode 2483 - Minimum Penalty for a Shop
# https://leetcode.com/problems/minimum-penalty-for-a-shop/

# @param {String} customers
# @return {Integer}
def best_closing_time(customers)
  n = customers.length
  penalty = 0
  customers.each_char { |c| penalty += 1 if c == "Y" }
  best = penalty
  ans = 0
  (0...n).each do |i|
    if customers[i] == "Y"
      penalty -= 1
    else
      penalty += 1
    end
    if penalty < best
      best = penalty
      ans = i + 1
    end
  end
  ans
end
