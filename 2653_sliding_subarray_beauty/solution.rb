# LeetCode 2653 - Sliding Subarray Beauty
# https://leetcode.com/problems/sliding-subarray-beauty/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} x
# @return {Integer[]}
def get_subarray_beauty(nums, k, x)
  freq = Array.new(101, 0)
  ans = Array.new(nums.length - k + 1, 0)
  nums.each_with_index do |num, i|
    freq[num + 50] += 1
    freq[nums[i - k] + 50] -= 1 if i >= k
    next if i < k - 1

    need = x
    val = 0
    50.times do |j|
      need -= freq[j]
      if need <= 0
        val = j - 50
        break
      end
    end
    ans[i - k + 1] = val
  end
  ans
end
