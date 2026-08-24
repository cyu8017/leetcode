# LeetCode 3984 - Divisible Game
# https://leetcode.com/problems/divisible-game/

# @param {Integer[]} nums
# @return {Integer}
def divisible_game(nums)
  candidates = { 2 => true }
  nums.each do |value|
    divisor = 2
    while divisor * divisor <= value
      if value % divisor == 0
        candidates[divisor] = true
        candidates[value / divisor] = true
      end
      divisor += 1
    end
    candidates[value] = true if value > 1
  end
  best_score = -(1 << 62)
  best_k = 0
  candidates.keys.each do |k|
    ending = 0
    score = 0
    nums.each_with_index do |value, i|
      contribution = value % k == 0 ? value : -value
      if i == 0 || ending + contribution < contribution
        ending = contribution
      else
        ending += contribution
      end
      score = ending if i == 0 || ending > score
    end
    if score > best_score || (score == best_score && k < best_k)
      best_score = score
      best_k = k
    end
  end
  mod = 1_000_000_007
  answer = (best_score % mod) * best_k % mod
  answer += mod if answer < 0
  answer
end
