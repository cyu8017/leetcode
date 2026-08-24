# LeetCode 3184 - Count Pairs That Form a Complete Day I
# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/

# @param {Integer[]} hours
# @return {Integer}
def count_complete_day_pairs(hours)
  cnt = Array.new(24, 0)
  ans = 0
  hours.each do |x|
    ans += cnt[(24 - x % 24) % 24]
    cnt[x % 24] += 1
  end
  ans
end
