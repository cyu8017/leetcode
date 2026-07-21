# LeetCode 1864 - Minimum Number of Swaps to Make the Binary String Alternating
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/

# @param {String} s
# @return {Integer}
def min_swaps(s)
  zeros = s.count("0")
  ones = s.length - zeros
  return -1 if (zeros - ones).abs > 1

  mismatches = lambda do |pattern|
    s.each_char.with_index.count { |ch, i| ch != pattern[i % 2] } / 2
  end

  return [mismatches.call("01"), mismatches.call("10")].min if zeros == ones
  return mismatches.call("01") if zeros > ones

  mismatches.call("10")
end
