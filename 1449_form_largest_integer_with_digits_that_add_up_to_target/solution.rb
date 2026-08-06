# LeetCode 1449 - Form Largest Integer With Digits That Add Up To Target
# https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

def largest_number(cost, target)
  dp = Array.new(target + 1)
  dp[0] = ''
  (1..target).each do |total|
    best = nil
    (1..9).each do |digit|
      price = cost[digit - 1]
      next unless total >= price && !dp[total - price].nil?
      candidate = digit.to_s + dp[total - price]
      best = candidate if best.nil? || [candidate.length, candidate] > [best.length, best]
    end
    dp[total] = best
  end
  dp[target] || '0'
end
