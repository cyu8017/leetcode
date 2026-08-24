# LeetCode 2145 - Count the Hidden Sequences
# https://leetcode.com/problems/count-the-hidden-sequences/

# @param {Integer[]} differences
# @param {Integer} lower
# @param {Integer} upper
# @return {Integer}
def number_of_arrays(differences, lower, upper)
  cur = 0
  mn = 0
  mx = 0
  differences.each do |d|
    cur += d
    mn = [mn, cur].min
    mx = [mx, cur].max
  end
  res = (upper - lower) - (mx - mn) + 1
  res < 0 ? 0 : res
end
