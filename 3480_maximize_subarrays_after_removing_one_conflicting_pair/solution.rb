# LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

# @param {Integer} n
# @param {Integer[][]} conflicting_pairs
# @return {Integer}
def max_subarrays(n, conflicting_pairs)
  m = conflicting_pairs.length
  best = 0
  (0...m).each do |skip|
    right_limit = Array.new(n + 2, n + 1)
    (0...m).each do |i|
      next if i == skip

      a = conflicting_pairs[i][0]
      b = conflicting_pairs[i][1]
      a, b = b, a if a > b
      right_limit[a] = b if b < right_limit[a]
    end
    min_right = n + 1
    cnt = 0
    n.downto(1) do |l|
      min_right = right_limit[l] if right_limit[l] < min_right
      cnt += min_right - l
    end
    best = cnt if cnt > best
  end
  best
end
