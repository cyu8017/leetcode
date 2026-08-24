# LeetCode 3141 - Maximum Hamming Distances
# https://leetcode.com/problems/maximum-hamming-distances/

# @param {Integer[]} nums
# @param {Integer} m
# @return {Integer[]}
def max_hamming_distances(nums, m)
  dist = Array.new(1 << m, -1)
  q = []
  nums.each do |x|
    dist[x] = 0
    q << x
  end
  k = 1
  until q.empty?
    t = []
    q.each do |x|
      m.times do |i|
        y = x ^ (1 << i)
        if dist[y] == -1
          dist[y] = k
          t << y
        end
      end
    end
    q = t
    k += 1
  end
  nums.map { |x| m - dist[x ^ ((1 << m) - 1)] }
end
