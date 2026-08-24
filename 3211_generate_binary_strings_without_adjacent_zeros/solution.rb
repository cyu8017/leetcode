# LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

# @param {Integer} n
# @return {String[]}
def valid_strings(n)
  ans = []
  t = []
  dfs = lambda do |i|
    if i >= n
      ans << t.join
      return
    end
    (0...2).each do |j|
      if (j == 0 && (i == 0 || t[i - 1] == "1")) || j == 1
        t << j.to_s
        dfs.call(i + 1)
        t.pop
      end
    end
  end
  dfs.call(0)
  ans
end
