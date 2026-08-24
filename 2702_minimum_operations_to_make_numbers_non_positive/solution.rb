# LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
# https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

# @param {Integer[]} nums
# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def min_operations(nums, x, y)
  lo = 0
  hi = 0
  nums.each do |v|
    a = (v + y - 1) / y
    b = (v + x - 1) / x
    hi = [hi, a, b].max
  end
  hi += nums.length
  ok = lambda do |ops|
    extra = 0
    nums.each do |v|
      remain = v - ops * y
      extra += (remain + (x - y) - 1) / (x - y) if remain > 0
    end
    extra <= ops
  end
  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end

def solve(*args)
  min_operations(*args)
end
