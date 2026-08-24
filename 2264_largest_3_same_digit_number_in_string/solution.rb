# LeetCode 2264 - Largest 3-Same-Digit Number in String
# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

# @param {String} num
# @return {String}
def largest_good_integer(num)
  best = ""
  (0..(num.length - 3)).each do |i|
    next unless num[i] == num[i + 1] && num[i + 1] == num[i + 2]

    cand = num[i, 3]
    best = cand if cand > best
  end
  best
end
