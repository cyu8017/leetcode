# LeetCode 1362 - Closest Divisors
# https://leetcode.com/problems/closest-divisors/

def closest_divisors(num)
  best = nil
  [num + 1, num + 2].each do |x|
    a = Math.sqrt(x).to_i
    while a >= 1
      if x % a == 0
        pair = [a, x / a]
        best = pair if best.nil? || pair[1] - pair[0] < best[1] - best[0]
        break
      end
      a -= 1
    end
  end
  best
end
