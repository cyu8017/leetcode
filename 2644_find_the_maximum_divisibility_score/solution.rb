# LeetCode 2644 - Find the Maximum Divisibility Score
# https://leetcode.com/problems/find-the-maximum-divisibility-score/

# @param {Integer[]} nums
# @param {Integer[]} divisors
# @return {Integer}
def max_div_score(nums, divisors)
  best = divisors[0]
  best_score = -1
  divisors.each do |d|
    score = 0
    nums.each { |x| score += 1 if x % d == 0 }
    if score > best_score || (score == best_score && d < best)
      best_score = score
      best = d
    end
  end
  best
end
