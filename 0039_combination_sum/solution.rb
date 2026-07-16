# LeetCode 0039 - Combination Sum
# https://leetcode.com/problems/combination-sum/

# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum(candidates, target)
  result = []

  backtrack = lambda do |start, remaining, path|
    if remaining == 0
      result << path.dup
      return
    end
    return if remaining < 0

    (start...candidates.length).each do |i|
      path << candidates[i]
      backtrack.call(i, remaining - candidates[i], path)
      path.pop
    end
  end

  backtrack.call(0, target, [])
  result
end
