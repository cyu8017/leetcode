# LeetCode 3896 - Minimum Operations to Transform Array into Alternating Prime
# https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

MX3896 = 200000
$is_prime3896 = nil
$primes3896 = nil

def init3896
  return unless $is_prime3896.nil?
  $is_prime3896 = Array.new(MX3896 + 1, true)
  $is_prime3896[0] = $is_prime3896[1] = false
  i = 2
  while i * i <= MX3896
    if $is_prime3896[i]
      j = i * i
      while j <= MX3896
        $is_prime3896[j] = false
        j += i
      end
    end
    i += 1
  end
  $primes3896 = []
  (2..MX3896).each { |x| $primes3896 << x if $is_prime3896[x] }
end

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  init3896
  ans = 0
  nums.each_with_index do |x, i|
    if i.even?
      lo = 0
      hi = $primes3896.length
      while lo < hi
        mid = (lo + hi) >> 1
        if $primes3896[mid] < x
          lo = mid + 1
        else
          hi = mid
        end
      end
      ans += $primes3896[lo] - x
    elsif $is_prime3896[x]
      ans += x == 2 ? 2 : 1
    end
  end
  ans
end
