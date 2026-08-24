# LeetCode 3854 - Minimum Operations to Make Array Parity Alternating
# https://leetcode.com/problems/minimum-operations-to-make-array-parity-alternating/

# @param {Integer[]} nums
# @return {Integer[]}
def make_parity_alternating(nums)
  return [0, 0] if nums.length == 1
  mn = nums.min
  mx = nums.max
  f = lambda do |k, mn_v, mx_v|
    cnt = 0
    a = Float::INFINITY
    b = -Float::INFINITY
    nums.each_with_index do |x, i|
      if ((x - i) & 1) != k
        cnt += 1
        if x == mn_v
          x += 1
        elsif x == mx_v
          x -= 1
        end
      end
      a = [a, x].min
      b = [b, x].max
    end
    [cnt, [1, (b - a).to_i].max]
  end
  r0 = f.call(0, mn, mx)
  r1 = f.call(1, mn, mx)
  return r0[0] < r1[0] ? r0 : r1 if r0[0] != r1[0]
  r0[1] <= r1[1] ? r0 : r1
end
