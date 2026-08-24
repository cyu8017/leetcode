# LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

# @param {Integer[]} nums
# @return {Integer}
def minimum_difference(nums)
  n = nums.length / 3
  left = Array.new(nums.length, 0)
  right = Array.new(nums.length, 0)
  hmax = []
  push_max = lambda do |x|
    hmax << x
    i = hmax.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if hmax[p] >= hmax[i]

      hmax[p], hmax[i] = hmax[i], hmax[p]
      i = p
    end
  end
  pop_max = lambda do
    top = hmax[0]
    last = hmax.pop
    if hmax.empty?
      return top
    end

    hmax[0] = last
    i = 0
    loop do
      l = i * 2 + 1
      r = l + 1
      s = i
      s = l if l < hmax.length && hmax[l] > hmax[s]
      s = r if r < hmax.length && hmax[r] > hmax[s]
      break if s == i

      hmax[s], hmax[i] = hmax[i], hmax[s]
      i = s
    end
    top
  end

  sum = 0
  n.times do |i|
    push_max.call(nums[i])
    sum += nums[i]
  end
  left[n - 1] = sum
  (n...(2 * n)).each do |i|
    push_max.call(nums[i])
    sum += nums[i]
    sum -= pop_max.call
    left[i] = sum
  end

  hmin = []
  push_min = lambda do |x|
    hmin << x
    i = hmin.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if hmin[p] <= hmin[i]

      hmin[p], hmin[i] = hmin[i], hmin[p]
      i = p
    end
  end
  pop_min = lambda do
    top = hmin[0]
    last = hmin.pop
    if hmin.empty?
      return top
    end

    hmin[0] = last
    i = 0
    loop do
      l = i * 2 + 1
      r = l + 1
      s = i
      s = l if l < hmin.length && hmin[l] < hmin[s]
      s = r if r < hmin.length && hmin[r] < hmin[s]
      break if s == i

      hmin[s], hmin[i] = hmin[i], hmin[s]
      i = s
    end
    top
  end

  sum = 0
  (nums.length - 1).downto(2 * n) do |i|
    push_min.call(nums[i])
    sum += nums[i]
  end
  right[2 * n] = sum
  (2 * n - 1).downto(n) do |i|
    push_min.call(nums[i])
    sum += nums[i]
    sum -= pop_min.call
    right[i] = sum
  end
  ans = left[n - 1] - right[n]
  (n...(2 * n)).each { |i| ans = [ans, left[i] - right[i + 1]].min }
  ans
end
