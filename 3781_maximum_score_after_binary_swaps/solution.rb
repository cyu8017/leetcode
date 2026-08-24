# LeetCode 3781 - Maximum Score After Binary Swaps
# https://leetcode.com/problems/maximum-score-after-binary-swaps/

class ScoreHeap
  def initialize
    @a = []
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  private

  def up(i)
    a = @a
    while i > 0
      p = (i - 1) >> 1
      break if a[i] <= a[p]
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
      s = l if l < n && a[l] > a[s]
      s = r if r < n && a[r] > a[s]
      break if s == i
      a[i], a[s] = a[s], a[i]
      i = s
    end
  end
end

# @param {Integer[]} nums
# @param {String} s
# @return {Integer}
def maximum_score(nums, s)
  ans = 0
  pq = ScoreHeap.new
  nums.each_with_index do |x, i|
    pq.push(x)
    ans += pq.pop if s[i] == "1"
  end
  ans
end
