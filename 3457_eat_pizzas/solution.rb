# LeetCode 3457 - Eat Pizzas!
# https://leetcode.com/problems/eat-pizzas/

# @param {Integer[]} pizzas
# @return {Integer}
def max_weight(pizzas)
  pizzas = pizzas.sort
  n = pizzas.length
  days = n / 4
  ans = 0
  odd_days = (days + 1) / 2
  even_days = days / 2
  idx = n - 1
  odd_days.times do
    ans += pizzas[idx]
    idx -= 1
  end
  even_days.times do
    idx -= 1
    ans += pizzas[idx]
    idx -= 1
  end
  ans
end
