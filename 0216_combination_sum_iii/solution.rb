# LeetCode 0216 - Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/

# @param {Integer} k
# @param {Integer} n
# @return {Integer[][]}
def combination_sum3(k, n)
  result = []

  backtrack = lambda do |start, remaining, path|
    if path.length == k
      result << path.dup if remaining == 0
      return
    end
    return if remaining <= 0 || path.length >= k

    (start..9).each do |num|
      break if num > remaining

      path << num
      backtrack.call(num + 1, remaining - num, path)
      path.pop
    end
  end

  backtrack.call(1, n, [])
  result
end
