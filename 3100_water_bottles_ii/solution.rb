# LeetCode 3100 - Water Bottles II
# https://leetcode.com/problems/water-bottles-ii/

# @param {Integer} num_bottles
# @param {Integer} num_exchange
# @return {Integer}
def max_bottles_drunk(num_bottles, num_exchange)
  ans = num_bottles
  while num_bottles >= num_exchange
    num_bottles -= num_exchange
    num_exchange += 1
    ans += 1
    num_bottles += 1
  end
  ans
end
