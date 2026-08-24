# LeetCode 3843 - First Element with Unique Frequency
# https://leetcode.com/problems/first-element-with-unique-frequency/

# @param {Integer[]} nums
# @return {Integer}
def first_unique_freq(nums)
  cnt = Hash.new(0)
  nums.each { |x| cnt[x] += 1 }
  freq = Hash.new(0)
  cnt.each_value { |v| freq[v] += 1 }
  nums.each { |x| return x if freq[cnt[x]] == 1 }
  -1
end
