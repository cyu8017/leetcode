# LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def count_k_constraint_substrings(s, k)
  ans = 0
  n = s.length
  (0...n).each do |i|
    z = o = 0
    (i...n).each do |j|
      if s[j] == "0"
        z += 1
      else
        o += 1
      end
      if z <= k || o <= k
        ans += 1
      else
        break
      end
    end
  end
  ans
end
