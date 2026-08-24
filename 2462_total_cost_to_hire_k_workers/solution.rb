# LeetCode 2462 - Total Cost to Hire K Workers
# https://leetcode.com/problems/total-cost-to-hire-k-workers/

# @param {Integer[]} costs
# @param {Integer} k
# @param {Integer} candidates
# @return {Integer}
def total_cost(costs, k, candidates)
  n = costs.length
  left_h = []
  right_h = []
  l = 0
  r = n - 1

  heap_push = lambda do |heap, item|
    heap << item
    i = heap.length - 1
    while i > 0
      p = (i - 1) / 2
      break if heap[p] <= heap[i]

      heap[p], heap[i] = heap[i], heap[p]
      i = p
    end
  end

  heap_pop = lambda do |heap|
    top = heap[0]
    last = heap.pop
    return top if heap.empty?

    heap[0] = last
    i = 0
    loop do
      smallest = i
      left = 2 * i + 1
      right = 2 * i + 2
      smallest = left if left < heap.length && heap[left] < heap[smallest]
      smallest = right if right < heap.length && heap[right] < heap[smallest]
      break if smallest == i

      heap[i], heap[smallest] = heap[smallest], heap[i]
      i = smallest
    end
    top
  end

  while l <= r && left_h.length < candidates
    heap_push.call(left_h, [costs[l], l])
    l += 1
  end
  while r >= l && right_h.length < candidates
    heap_push.call(right_h, [costs[r], r])
    r -= 1
  end
  ans = 0
  k.times do
    use_left = false
    if !left_h.empty? && !right_h.empty?
      lt = left_h[0]
      rt = right_h[0]
      use_left = true if lt[0] < rt[0] || (lt[0] == rt[0] && lt[1] <= rt[1])
    elsif !left_h.empty?
      use_left = true
    end
    if use_left
      ans += heap_pop.call(left_h)[0]
      if l <= r
        heap_push.call(left_h, [costs[l], l])
        l += 1
      end
    else
      ans += heap_pop.call(right_h)[0]
      if l <= r
        heap_push.call(right_h, [costs[r], r])
        r -= 1
      end
    end
  end
  ans
end
