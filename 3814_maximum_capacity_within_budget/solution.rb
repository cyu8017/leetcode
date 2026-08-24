# LeetCode 3814 - Maximum Capacity Within Budget
# https://leetcode.com/problems/maximum-capacity-within-budget/

class CapHeap
  def initialize
    @a = []
  end

  def size
    @a.length
  end

  def peek
    @a[0]
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  private

  def cmp(a, b)
    return b[0] - a[0] if a[0] != b[0]
    b[1] - a[1]
  end

  def up(i)
    a = @a
    while i > 0
      p = (i - 1) >> 1
      break if cmp(a[i], a[p]) >= 0
      a[i], a[p] = a[p], a[i]
      i = p
    end
  end

  def down(i)
    a = @a
    n = a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && cmp(a[l], a[s]) < 0
      s = r if r < n && cmp(a[r], a[s]) < 0
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
end

# @param {Integer[]} costs
# @param {Integer[]} capacity
# @param {Integer} budget
# @return {Integer}
def max_capacity(costs, capacity, budget)
  arr = []
  (0...costs.length).each { |k| arr << [costs[k], capacity[k]] if costs[k] < budget }
  return 0 if arr.empty?
  arr.sort_by! { |x| x[0] }
  m = arr.length
  alive = Array.new(m, true)
  h = CapHeap.new
  (0...m).each { |i| h.push([arr[i][1], i]) }
  h.pop while h.size > 0 && !alive[h.peek[1]]
  ans = h.peek[0]
  i = 0
  j = m - 1
  while i < j
    alive[i] = false
    while i < j && arr[i][0] + arr[j][0] >= budget
      alive[j] = false
      j -= 1
    end
    h.pop while h.size > 0 && !alive[h.peek[1]]
    ans = [ans, arr[i][1] + h.peek[0]].max if h.size > 0
    i += 1
  end
  ans
end
