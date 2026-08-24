# LeetCode 3287 - Find the Maximum Sequence Value of Array
# https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_value(nums, k)
  n = nums.length
  maxv = 128
  left = Array.new(n + 1) { Array.new(k + 1) { Array.new(maxv, false) } }
  left[0][0][0] = true
  n.times do |i|
    (0..k).each do |j|
      maxv.times do |v|
        next unless left[i][j][v]

        left[i + 1][j][v] = true
        left[i + 1][j + 1][v | nums[i]] = true if j < k
      end
    end
  end
  right = Array.new(n + 1) { Array.new(k + 1) { Array.new(maxv, false) } }
  right[n][0][0] = true
  (n - 1).downto(0) do |i|
    (0..k).each do |j|
      maxv.times do |v|
        next unless right[i + 1][j][v]

        right[i][j][v] = true
        right[i][j + 1][v | nums[i]] = true if j < k
      end
    end
  end
  ans = 0
  (k..(n - k)).each do |mid|
    maxv.times do |a|
      next unless left[mid][k][a]

      maxv.times do |b|
        ans = a ^ b if right[mid][k][b] && (a ^ b) > ans
      end
    end
  end
  ans
end
