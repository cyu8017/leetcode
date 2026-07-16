# LeetCode 0077 - Combinations
# https://leetcode.com/problems/combinations/

# @param {Integer} n
# @param {Integer} k
# @return {Integer[][]}
def combine(n, k)
  result = []
  path = []

  backtrack = lambda do |start|
    if path.length == k
      result << path.dup
      return
    end

    remaining = k - path.length
    (start..(n - remaining + 1)).each do |i|
      path << i
      backtrack.call(i + 1)
      path.pop
    end
  end

  backtrack.call(1)
  result
end
