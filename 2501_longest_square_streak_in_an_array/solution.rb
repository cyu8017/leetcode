# LeetCode 2501 - Longest Square Streak in an Array
# https://leetcode.com/problems/longest-square-streak-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def longest_square_streak(nums)
  seen = {}
  nums.each { |x| seen[x] = true }
  best = -1
  nums.each do |x|
    next unless seen[x]

    length = 0
    cur = x
    while seen[cur]
      length += 1
      seen.delete(cur)
      break if cur > 100_000

      cur = cur * cur
    end
    best = length if length >= 2 && length > best
  end
  best
end
