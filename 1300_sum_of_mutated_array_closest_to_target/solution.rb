# LeetCode 1300 - Sum Of Mutated Array Closest To Target
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

def find_best_value(arr, target)
  lo = 0
  hi = arr.max
  while lo < hi
    mid = (lo + hi) / 2
    s = arr.sum { |x| [x, mid].min }
    if s < target
      lo = mid + 1
    else
      hi = mid
    end
  end
  before = arr.sum { |x| [x, lo - 1].min }
  after = arr.sum { |x| [x, lo].min }
  target - before <= after - target ? lo - 1 : lo
end
