# LeetCode 3817 - Good Indices in a Digit String
# https://leetcode.com/problems/good-indices-in-a-digit-string/

# @param {String} s
# @return {Integer[]}
def good_indices(s)
  ans = []
  (0...s.length).each do |i|
    t = i.to_s
    k = t.length
    ans << i if i + 1 - k >= 0 && s[i + 1 - k, k] == t
  end
  ans
end
