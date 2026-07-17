# LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

# @param {Integer} n
# @return {Integer[]}
def construct_distanced_sequence(n)
  ans = Array.new(2 * n - 1, 0)
  used = Array.new(n + 1, false)

  backtrack = lambda do |i|
    i += 1 while i < ans.length && ans[i] != 0
    return true if i == ans.length
    n.downto(1) do |value|
      next if used[value]
      if value == 1
        ans[i] = 1
        used[1] = true
        return true if backtrack.call(i + 1)
        used[1] = false
        ans[i] = 0
      else
        j = i + value
        if j < ans.length && ans[j].zero?
          ans[i] = value
          ans[j] = value
          used[value] = true
          return true if backtrack.call(i + 1)
          used[value] = false
          ans[i] = 0
          ans[j] = 0
        end
      end
    end
    false
  end

  backtrack.call(0)
  ans
end
