# LeetCode 1383 - Maximum Performance Of A Team
# https://leetcode.com/problems/maximum-performance-of-a-team/

def max_performance(n, speed, efficiency, k)
  heap = []
  total = 0
  ans = 0
  efficiency.zip(speed).sort_by { |e, _s| -e }.each do |e, s|
    heap << s
    heap.sort!
    total += s
    if heap.length > k
      total -= heap.shift
    end
    ans = [ans, total * e].max
  end
  ans % 1_000_000_007
end
