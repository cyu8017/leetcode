# LeetCode 2964 - Number of Divisible Triplet Sums
# https://leetcode.com/problems/number-of-divisible-triplet-sums/

# @param {Integer[]} nums
# @param {Integer} d
# @return {Integer}
def divisible_triplet_count(nums, d)
  n = nums.length
  ans = 0
  n.times do |i|
    freq = Hash.new(0)
    (i + 1...n).each do |j|
      need = (d - (nums[i] + nums[j]) % d) % d
      ans += freq[need]
      freq[nums[j] % d] += 1
    end
  end
  ans
end

def solve(*args)
  divisible_triplet_count(*args)
end
