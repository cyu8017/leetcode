# LeetCode 2615 - Sum of Distances
# https://leetcode.com/problems/sum-of-distances/

# @param {Integer[]} nums
# @return {Integer[]}
def distance(nums)
  n = nums.length
  ans = Array.new(n, 0)
  pos = {}
  nums.each_with_index do |x, i|
    pos[x] ||= []
    pos[x] << i
  end
  pos.each_value do |idxs|
    m = idxs.length
    pref = Array.new(m + 1, 0)
    m.times { |i| pref[i + 1] = pref[i] + idxs[i] }
    m.times do |j|
      idx = idxs[j]
      left = j * idx - pref[j]
      right = pref[m] - pref[j + 1] - (m - 1 - j) * idx
      ans[idx] = left + right
    end
  end
  ans
end
