# LeetCode 2808 - Minimum Seconds to Equalize a Circular Array
# https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/

# @param {Integer[]} nums
# @return {Integer}
def minimum_seconds(nums)
  n = nums.length
  pos = {}
  nums.each_with_index { |v, i| (pos[v] ||= []) << i }
  ans = n
  pos.each_value do |p|
    max_gap = 0
    p.each_index do |i|
      gap = i + 1 < p.length ? p[i + 1] - p[i] : p[0] + n - p[i]
      max_gap = [max_gap, gap / 2].max
    end
    ans = [ans, max_gap].min
  end
  ans
end
