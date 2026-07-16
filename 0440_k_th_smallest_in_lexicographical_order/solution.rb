# LeetCode 0440 - K-th Smallest in Lexicographical Order
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution
  def find_kth_number(n, k)
    current = 1
    k -= 1

    while k.positive?
      steps = count_steps(n, current, current + 1)
      if steps <= k
        current += 1
        k -= steps
      else
        current *= 10
        k -= 1
      end
    end

    current
  end

  alias_method :findKthNumber, :find_kth_number

  private

  def count_steps(n, first, last)
    steps = 0
    while first <= n
      steps += [n + 1, last].min - first
      first *= 10
      last *= 10
    end
    steps
  end
end
