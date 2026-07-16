# LeetCode 0040 - Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum2(candidates, target)
  candidates.sort!
  result = []

  backtrack = lambda do |start, remaining, path|
    if remaining == 0
      result << path.dup
      return
    end
    return if remaining < 0

    (start...candidates.length).each do |i|
      next if i > start && candidates[i] == candidates[i - 1]

      path << candidates[i]
      backtrack.call(i + 1, remaining - candidates[i], path)
      path.pop
    end
  end

  backtrack.call(0, target, [])
  result
end
