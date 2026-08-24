# LeetCode 3316 - Find Maximum Removals From Source String
# https://leetcode.com/problems/find-maximum-removals-from-source-string/

# @param {Integer} remove_first
# @param {String} source
# @param {String} pattern
# @param {Integer[]} target_indices
# @param {Integer} n
# @return {Boolean}
def removals_ok(remove_first, source, pattern, target_indices, n)
  mark = Array.new(n, false)
  remove_first.times { |i| mark[target_indices[i]] = true }
  j = 0
  i = 0
  while i < n && j < pattern.length
    j += 1 if !mark[i] && source[i] == pattern[j]
    i += 1
  end
  j == pattern.length
end

# @param {String} source
# @param {String} pattern
# @param {Integer[]} target_indices
# @return {Integer}
def max_removals(source, pattern, target_indices)
  n = source.length
  lo = 0
  hi = target_indices.length
  while lo < hi
    mid = (lo + hi + 1) >> 1
    if removals_ok(mid, source, pattern, target_indices, n)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
