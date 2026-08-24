# LeetCode 2405 - Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/

# @param {String} s
# @return {Integer}
def partition_string(s)
  ans = 1
  seen = 0
  s.each_char do |c|
    bit = 1 << (c.ord - 97)
    if (seen & bit) != 0
      ans += 1
      seen = 0
    end
    seen |= bit
  end
  ans
end
