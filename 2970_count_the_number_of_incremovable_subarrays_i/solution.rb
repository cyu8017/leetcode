# LeetCode 2970 - Count the Number of Incremovable Subarrays I
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/

# @param {Integer[]} nums
# @return {Integer}
def incremovable_subarray_count(nums)
  n = nums.length
  ans = 0
  n.times do |i|
    i.upto(n - 1) do |j|
      prev = -1
      ok = true
      n.times do |t|
        next if t >= i && t <= j
        if nums[t] <= prev
          ok = false
          break
        end
        prev = nums[t]
      end
      ans += 1 if ok
    end
  end
  ans
end
