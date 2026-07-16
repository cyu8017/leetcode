# LeetCode 0047 - Permutations II
# https://leetcode.com/problems/permutations-ii/

# @param {Integer[]} nums
# @return {Integer[][]}
def permute_unique(nums)
  nums = nums.sort
  result = []
  path = []
  used = Array.new(nums.length, false)

  backtrack = lambda do
    if path.length == nums.length
      result << path.dup
      return
    end

    (0...nums.length).each do |i|
      next if used[i]
      if i > 0 && nums[i] == nums[i - 1] && !used[i - 1]
        next
      end

      used[i] = true
      path << nums[i]
      backtrack.call
      path.pop
      used[i] = false
    end
  end

  backtrack.call
  result
end
