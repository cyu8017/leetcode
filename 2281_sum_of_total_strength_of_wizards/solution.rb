# LeetCode 2281 - Sum of Total Strength of Wizards
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/

# @param {Integer[]} strength
# @return {Integer}
def total_strength(strength)
  mod = 1_000_000_007
  n = strength.length
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  stack = []
  n.times do |i|
    stack.pop while !stack.empty? && strength[stack[-1]] >= strength[i]
    left[i] = stack.empty? ? -1 : stack[-1]
    stack << i
  end
  stack = []
  (n - 1).downto(0) do |i|
    stack.pop while !stack.empty? && strength[stack[-1]] > strength[i]
    right[i] = stack.empty? ? n : stack[-1]
    stack << i
  end
  pref = Array.new(n + 1, 0)
  pref_pref = Array.new(n + 2, 0)
  n.times { |i| pref[i + 1] = (pref[i] + strength[i]) % mod }
  (0..n).each { |i| pref_pref[i + 1] = (pref_pref[i] + pref[i]) % mod }
  ans = 0
  n.times do |i|
    l = left[i] + 1
    r = right[i] - 1
    left_sum = (pref_pref[i + 1] - pref_pref[l] + mod) % mod
    right_sum = (pref_pref[r + 2] - pref_pref[i + 1] + mod) % mod
    left_cnt = i - l + 1
    right_cnt = r - i + 1
    contrib = (left_cnt * right_sum % mod - right_cnt * left_sum % mod + mod) % mod
    ans = (ans + contrib * strength[i] % mod) % mod
  end
  ans
end
