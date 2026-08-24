# LeetCode 3171 - Find Subarray With Bitwise OR Closest to K
# https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def minimum_difference(nums, k)
  mx = nums.max
  m = mx == 0 ? 1 : 32 - leading_zero_count(mx)
  cnt = Array.new(m, 0)
  ans = 10**18
  s = 0
  i = 0
  nums.each_with_index do |x, j|
    s |= x
    ans = [ans, (s - k).abs].min
    (0...m).each do |h|
      cnt[h] += 1 if ((x >> h) & 1) != 0
    end
    while i < j && s > k
      y = nums[i]
      (0...m).each do |h|
        if ((y >> h) & 1) != 0
          cnt[h] -= 1
          s ^= 1 << h if cnt[h] == 0
        end
      end
      ans = [ans, (s - k).abs].min
      i += 1
    end
  end
  ans
end

def leading_zero_count(x)
  return 32 if x == 0
  n = 0
  31.downto(0) do |bit|
    break if ((x >> bit) & 1) != 0
    n += 1
  end
  n
end
