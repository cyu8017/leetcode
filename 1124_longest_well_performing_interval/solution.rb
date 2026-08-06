# LeetCode 1124 - Longest Well-Performing Interval
# https://leetcode.com/problems/longest-well-performing-interval/

# @param {Integer[]} hours
# @return {Integer}
def longest_wpi(hours)
  score = 0
  seen = {}
  ans = 0
  hours.each_with_index do |h, i|
    score += h > 8 ? 1 : -1
    if score > 0
      ans = i + 1
    else
      seen[score] = i unless seen.key?(score)
      ans = [ans, i - seen[score - 1]].max if seen.key?(score - 1)
    end
  end
  ans
end
