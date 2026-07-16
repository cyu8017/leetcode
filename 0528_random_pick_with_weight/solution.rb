# LeetCode 0528 - Random Pick with Weight
# https://leetcode.com/problems/random-pick-with-weight/

$uniform = ->(_a, _b) { 0 }

def set_uniform(uniform_fn)
  $uniform = uniform_fn
end

class Solution
  def initialize(w)
    @prefix = []
    total = 0
    w.each do |weight|
      total += weight
      @prefix << total
    end
    @total = total
  end

  def pick_index
    target = $uniform.call(0, @total).to_i
    target = @total - 1 if target >= @total
    bisect_right(@prefix, target)
  end

  alias_method :pickIndex, :pick_index

  private

  def bisect_right(arr, target)
    low = 0
    high = arr.length - 1
    while low < high
      mid = (low + high) / 2
      if arr[mid] <= target
        low = mid + 1
      else
        high = mid
      end
    end
    low
  end
end
