# LeetCode 2210 - Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def count_hill_valley(nums)
  compact = [nums[0]]
  (1...nums.length).each do |i|
    compact << nums[i] if nums[i] != compact[-1]
  end
  ans = 0
  i = 1
  while i + 1 < compact.length
    if (compact[i] > compact[i - 1] && compact[i] > compact[i + 1]) ||
       (compact[i] < compact[i - 1] && compact[i] < compact[i + 1])
      ans += 1
    end
    i += 1
  end
  ans
end
