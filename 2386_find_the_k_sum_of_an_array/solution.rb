# LeetCode 2386 - Find the K-Sum of an Array
# https://leetcode.com/problems/find-the-k-sum-of-an-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def k_sum(nums, k)
  total = 0
  n = nums.length
  abs_nums = Array.new(n, 0)
  (0...n).each do |i|
    if nums[i] >= 0
      total += nums[i]
      abs_nums[i] = nums[i]
    else
      abs_nums[i] = -nums[i]
    end
  end
  abs_nums.sort!
  h = []
  push = lambda do |item|
    h << item
    i = h.length - 1
    while i > 0
      p = (i - 1) >> 1
      break if h[p][0] >= h[i][0]
      h[p], h[i] = h[i], h[p]
      i = p
    end
  end
  pop = lambda do
    top = h[0]
    last = h.pop
    unless h.empty?
      h[0] = last
      i = 0
      loop do
        largest = i
        l = i * 2 + 1
        r = i * 2 + 2
        largest = l if l < h.length && h[l][0] > h[largest][0]
        largest = r if r < h.length && h[r][0] > h[largest][0]
        break if largest == i
        h[largest], h[i] = h[i], h[largest]
        i = largest
      end
    end
    top
  end
  push.call([total, 0])
  (k - 1).times do
    cur = pop.call
    s = cur[0]
    i = cur[1]
    next if i >= abs_nums.length
    push.call([s - abs_nums[i], i + 1])
    push.call([s - abs_nums[i] + abs_nums[i - 1], i + 1]) if i > 0
  end
  h[0][0]
end
