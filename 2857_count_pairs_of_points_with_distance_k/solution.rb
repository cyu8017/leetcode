# LeetCode 2857 - Count Pairs of Points With Distance k
# https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

# @param {Integer[][]} coordinates
# @param {Integer} k
# @return {Integer}
def count_pairs(coordinates, k)
  freq = {}
  ans = 0
  coordinates.each do |x, y|
    (0..k).each do |a|
      b = k - a
      ans += freq.fetch([x ^ a, y ^ b], 0)
    end
    key = [x, y]
    freq[key] = freq.fetch(key, 0) + 1
  end
  ans
end
