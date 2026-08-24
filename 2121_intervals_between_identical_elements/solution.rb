# LeetCode 2121 - Intervals Between Identical Elements
# https://leetcode.com/problems/intervals-between-identical-elements/

# @param {Integer[]} arr
# @return {Integer[]}
def get_distances(arr)
  n = arr.length
  pos = Hash.new { |h, k| h[k] = [] }
  n.times { |i| pos[arr[i]] << i }
  ans = Array.new(n, 0)
  pos.each_value do |idxs|
    m = idxs.length
    pref = Array.new(m + 1, 0)
    m.times { |i| pref[i + 1] = pref[i] + idxs[i] }
    m.times do |i|
      left = i * idxs[i] - pref[i]
      right = (pref[m] - pref[i + 1]) - (m - i - 1) * idxs[i]
      ans[idxs[i]] = left + right
    end
  end
  ans
end
