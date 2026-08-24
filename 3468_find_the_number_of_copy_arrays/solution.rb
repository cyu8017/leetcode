# LeetCode 3468 - Find the Number of Copy Arrays
# https://leetcode.com/problems/find-the-number-of-copy-arrays/

# @param {Integer[]} original
# @param {Integer[][]} bounds
# @return {Integer}
def count_arrays(original, bounds)
  n = original.length
  lo = bounds[0][0]
  hi = bounds[0][1]
  (1...n).each do |i|
    diff = original[i] - original[i - 1]
    lo2 = bounds[i][0]
    hi2 = bounds[i][1]
    nlo = lo + diff
    nhi = hi + diff
    nlo = lo2 if nlo < lo2
    nhi = hi2 if nhi > hi2
    return 0 if nlo > nhi

    lo = nlo
    hi = nhi
  end
  hi - lo + 1
end
