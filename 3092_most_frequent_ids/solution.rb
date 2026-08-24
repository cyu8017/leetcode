# LeetCode 3092 - Most Frequent IDs
# https://leetcode.com/problems/most-frequent-ids/

# @param {Integer[]} nums
# @param {Integer[]} freq
# @return {Integer[]}
def most_frequent_i_ds(nums, freq)
  n = nums.length
  cnt = {}
  lazy = Hash.new(0)
  ans = Array.new(n, 0)
  pq = []
  n.times do |i|
    x = nums[i]
    f = freq[i]
    old = cnt.fetch(x, 0)
    lazy[old] += 1
    neu = old + f
    cnt[x] = neu
    heap_push_neg(pq, -neu)
    while !pq.empty? && lazy[-pq[0]] > 0
      top = -heap_pop_neg(pq)
      lazy[top] -= 1
    end
    ans[i] = pq.empty? ? 0 : -pq[0]
  end
  ans
end

def heap_push_neg(a, x)
  a << x
  i = a.length - 1
  while i > 0
    p = (i - 1) >> 1
    break if a[i] >= a[p]
    a[i], a[p] = a[p], a[i]
    i = p
  end
end

def heap_pop_neg(a)
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
