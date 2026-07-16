# LeetCode 0254 - Factor Combinations
# https://leetcode.com/problems/factor-combinations/

# @param {Integer} n
# @return {Integer[][]}
def get_factors(n)
  result = []
  path = []

  backtrack = lambda do |remain, start|
    if start > remain
      result << path.dup if path.length > 1
      return
    end

    factor = start
    while factor * factor <= remain
      if remain % factor == 0
        path << factor
        backtrack.call(remain / factor, factor)
        path.pop
      end
      factor += 1
    end

    if path.any?
      path << remain
      result << path.dup if path.length > 1
      path.pop
    end
  end

  backtrack.call(n, 2)
  result
end
