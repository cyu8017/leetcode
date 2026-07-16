# LeetCode 0090 - Subsets II
# https://leetcode.com/problems/subsets-ii/

# @param {Integer[]} nums
# @return {Integer[][]}
def subsets_with_dup(nums)
  nums.sort!
  result = []

  backtrack = lambda do |start, path|
    result << path.dup
    (start...nums.length).each do |i|
      next if i > start && nums[i] == nums[i - 1]

      path << nums[i]
      backtrack.call(i + 1, path)
      path.pop
    end
  end

  backtrack.call(0, [])
  result
end
