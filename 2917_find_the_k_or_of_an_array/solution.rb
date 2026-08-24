# LeetCode 2917 - Find the K-or of an Array
# https://leetcode.com/problems/find-the-k-or-of-an-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_k_or(nums, k)
  ans = 0
  (0...31).each do |b|
    cnt = 0
    nums.each { |v| cnt += 1 if (v & (1 << b)) != 0 }
    ans |= 1 << b if cnt >= k
  end
  ans
end
