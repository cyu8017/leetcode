# LeetCode 0483 - Smallest Good Base
# https://leetcode.com/problems/smallest-good-base/

class Solution
  def smallest_good_base(n)
    num = n.to_i
    max_length = Math.log(num) / Math.log(2)
    max_length = max_length.to_i + 1
    (max_length).downto(2) do |length|
      low = 2
      high = num - 1
      while low <= high
        mid = (low + high) / 2
        total = 1
        power = 1
        ok = true
        (length - 1).times do
          power *= mid
          total += power
          if total > num
            ok = false
            break
          end
        end
        return mid.to_s if ok && total == num

        if !ok || total > num
          high = mid - 1
        else
          low = mid + 1
        end
      end
    end
    (num - 1).to_s
  end

  alias_method :smallestGoodBase, :smallest_good_base
end
