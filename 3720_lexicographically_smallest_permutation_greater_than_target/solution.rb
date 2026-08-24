# LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

# @param {String} s
# @param {String} target
# @return {String}
def lex_greater_permutation(s, target)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  n = s.length
  ans = Array.new(n, "")
  dfs = nil
  dfs = lambda do |pos, greater|
    return greater if pos == n
    start = greater ? 0 : (target[pos].ord - 97)
    (start...26).each do |c|
      next if cnt[c] == 0
      cnt[c] -= 1
      ans[pos] = (97 + c).chr
      ng = greater || c > (target[pos].ord - 97)
      return true if dfs.call(pos + 1, ng)
      cnt[c] += 1
    end
    false
  end
  return ans.join if dfs.call(0, false)
  ""
end
