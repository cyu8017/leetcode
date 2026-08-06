# LeetCode 1354 - Construct Target Array With Multiple Sums
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/

def is_possible(target)
  return target[0] == 1 if target.length == 1
  total = target.sum
  heap = target.sort.reverse
  loop do
    x = heap.shift
    rest = total - x
    return true if x == 1 || rest == 1
    return false if rest == 0 || x <= rest
    prev = x % rest
    return false if prev == 0
    total = rest + prev
    heap << prev
    heap.sort!.reverse!
  end
end
