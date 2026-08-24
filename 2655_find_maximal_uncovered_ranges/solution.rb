# LeetCode 2655 - Find Maximal Uncovered Ranges
# https://leetcode.com/problems/find-maximal-uncovered-ranges/

# @param {Integer} n
# @param {Integer[][]} ranges
# @return {Integer[][]}
def find_maximal_uncovered_ranges(n, ranges)
  ranges = ranges.sort_by { |r| r[0] }
  ans = []
  cur = 0
  ranges.each do |r|
    ans << [cur, r[0] - 1] if r[0] > cur
    cur = r[1] + 1 if r[1] + 1 > cur
  end
  ans << [cur, n - 1] if cur < n
  ans
end

def solve(*args)
  find_maximal_uncovered_ranges(*args)
end
