# LeetCode 0046 - Permutations
# https://leetcode.com/problems/permutations/

# @param {Integer[]} nums
# @return {Integer[][]}
def permute(nums)
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
