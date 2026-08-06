# LeetCode 1447 - Simplified Fractions
# https://leetcode.com/problems/simplified-fractions/

def simplified_fractions(n)
  (1...n).flat_map do |a|
    ((a + 1)..n).select { |b| a.gcd(b) == 1 }.map { |b| "#{a}/#{b}" }
  end
end
