# LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
# https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

# @param {String} hamsters
# @return {Integer}
def minimum_buckets(hamsters)
  b = hamsters.chars
  ans = 0
  b.each_index do |i|
    next unless b[i] == "H"
    next if i > 0 && b[i - 1] == "B"

    if i + 1 < b.length && b[i + 1] == "."
      b[i + 1] = "B"
      ans += 1
    elsif i > 0 && b[i - 1] == "."
      b[i - 1] = "B"
      ans += 1
    else
      return -1
    end
  end
  ans
end
