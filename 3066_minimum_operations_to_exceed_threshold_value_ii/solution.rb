# LeetCode 3066 - Minimum Operations to Exceed Threshold Value II
# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  pq = []
  nums.each { |x| heap_push(pq, x) }
  ans = 0
  while pq.length > 1 && pq[0] < k
    x = heap_pop(pq)
    y = heap_pop(pq)
    heap_push(pq, x * 2 + y)
    ans += 1
  end
  ans
end

def heap_push(a, x)
  a << x
  i = a.length - 1
  while i > 0
    p = (i - 1) >> 1
    break if a[i] >= a[p]
    a[i], a[p] = a[p], a[i]
    i = p
  end
end

def heap_pop(a)
  return nil if a.empty?
  top = a[0]
  last = a.pop
  if a.length > 0
    a[0] = last
    i = 0
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && a[l] < a[s]
      s = r if r < n && a[r] < a[s]
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
  top
end
