# LeetCode 0805 - Split Array With Same Average
# https://leetcode.com/problems/split-array-with-same-average/

# @param {Integer[]} nums
# @return {Boolean}
def split_array_same_average(nums)
  n = nums.length
  total = nums.sum
  nums = nums.sort
  memo = {}

  find = lambda do |target, count, index|
    key = [target, count, index]
    return memo[key] if memo.key?(key)
    if count == 0
      return memo[key] = (target == 0)
    end
    if index == n || count + index > n || target < 0
      return memo[key] = false
    end

    memo[key] = find.call(target - nums[index], count - 1, index + 1) ||
                find.call(target, count, index + 1)
  end

  (1...n).each do |size|
    return true if (total * size) % n == 0 && find.call(total * size / n, size, 0)
  end
  false
end
