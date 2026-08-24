# LeetCode 2200 - Find All K-Distant Indices in an Array
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

# @param {Integer[]} nums
# @param {Integer} key
# @param {Integer} k
# @return {Integer[]}
def find_k_distant_indices(nums, key, k)
  n = nums.length
  mark = Array.new(n, false)
  n.times do |i|
    next unless nums[i] == key

    l = [0, i - k].max
    r = [n - 1, i + k].min
    (l..r).each { |j| mark[j] = true }
  end
  ans = []
  n.times { |i| ans << i if mark[i] }
  ans
end
