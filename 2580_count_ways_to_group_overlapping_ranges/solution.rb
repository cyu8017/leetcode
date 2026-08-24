# LeetCode 2580 - Count Ways to Group Overlapping Ranges
# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/

# @param {Integer[][]} ranges
# @return {Integer}
def count_ways(ranges)
  mod = 1_000_000_007
  ranges = ranges.sort_by { |r| r[0] }
  groups = 0
  endi = -1
  ranges.each do |r|
    if r[0] > endi
      groups += 1
      endi = r[1]
    elsif r[1] > endi
      endi = r[1]
    end
  end
  ans = 1
  groups.times { ans = ans * 2 % mod }
  ans
end
