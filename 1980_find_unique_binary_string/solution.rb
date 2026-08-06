# LeetCode 1980 - Find Unique Binary String
# https://leetcode.com/problems/find-unique-binary-string/

# @param {String[]} nums
# @return {String}
def find_different_binary_string(nums)
  s = nums.to_h { |x| [x, true] }
  n = nums.length
  preferred = %w[11 101 00 10 01 000 001 010 011 100 110 111]
  preferred.each do |cand|
    return cand if cand.length == n && !s[cand]
  end
  (0...(1 << n)).each do |i|
    cand = i.to_s(2).rjust(n, "0")
    return cand unless s[cand]
  end
  "0" * n
end
