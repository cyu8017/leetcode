# LeetCode 4013 - Count Subarrays With Even Odd Ratio II
# https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-ii/

class BIT
  def initialize(n)
    @n = n
    @c = Array.new(n + 1, 0)
  end

  def update(x, delta)
    while x <= @n
      @c[x] += delta
      x += x & -x
    end
  end

  def query(x)
    s = 0
    while x > 0
      s += @c[x]
      x -= x & -x
    end
    s
  end
end

# @param {Integer[]} nums
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def count_ratio_subarrays(nums, a, b)
  n = nums.length
  s = Array.new(n + 1, 0)
  n.times do |i|
    s[i + 1] = if nums[i].odd?
                 s[i] + a
               else
                 s[i] - b
               end
  end
  st = s.sort
  uniq = 0
  st.each_with_index do |v, i|
    if uniq == 0 || v != st[uniq - 1]
      st[uniq] = v
      uniq += 1
    end
  end
  st = st[0...uniq]
  lower_bound = lambda do |arr, x|
    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) / 2
      if arr[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  bit = BIT.new(st.length + 1)
  ans = 0
  s.each do |v|
    x = lower_bound.call(st, v) + 1
    ans += bit.query(x)
    bit.update(x, 1)
  end
  ans
end
