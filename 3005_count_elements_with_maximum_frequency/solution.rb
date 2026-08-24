# LeetCode 3005 - Count Elements With Maximum Frequency
# https://leetcode.com/problems/count-elements-with-maximum-frequency/

# @param {Integer[]} nums
# @return {Integer}
def max_frequency_elements(nums)
  cnt = Array.new(101, 0)
  nums.each { |x| cnt[x] += 1 }
  mx = -1
  ans = 0
  cnt.each do |x|
    if mx < x
      mx = x
      ans = x
    elsif mx == x
      ans += x
    end
  end
  ans
end
