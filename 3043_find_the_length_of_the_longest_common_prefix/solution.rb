# LeetCode 3043 - Find the Length of the Longest Common Prefix
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer}
def longest_common_prefix(arr1, arr2)
  s = {}
  arr1.each do |x0|
    x = x0
    while x > 0
      s[x] = true
      x /= 10
    end
  end
  mx = 0
  arr2.each do |x0|
    x = x0
    while x > 0
      if s[x]
        mx = x if x > mx
        break
      end
      x /= 10
    end
  end
  mx > 0 ? mx.to_s.length : 0
end
