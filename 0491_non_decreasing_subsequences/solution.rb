# LeetCode 0491 - Non-decreasing Subsequences
# https://leetcode.com/problems/non-decreasing-subsequences/

require "set"

class Solution
  def find_subsequences(nums)
    result = Set.new

    backtrack = lambda do |start, path|
      result.add(path.dup) if path.length >= 2
      used = {}
      (start...nums.length).each do |index|
        next if used[nums[index]]
        next if !path.empty? && nums[index] < path[-1]

        used[nums[index]] = true
        path << nums[index]
        backtrack.call(index + 1, path)
        path.pop
      end
    end

    backtrack.call(0, [])
    result.to_a.sort
  end

  alias_method :findSubsequences, :find_subsequences
end
