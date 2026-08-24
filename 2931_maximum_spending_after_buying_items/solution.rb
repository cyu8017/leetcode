# LeetCode 2931 - Maximum Spending After Buying Items
# https://leetcode.com/problems/maximum-spending-after-buying-items/

# @param {Integer[][]} values
# @return {Integer}
def max_spending(values)
  m = values.length
  n = values[0].length
  idx = Array.new(m, n - 1)
  ans = 0
  day = 1
  total = m * n
  total.times do
    best_i = -1
    best_v = 10**18
    (0...m).each do |i|
      if idx[i] >= 0 && values[i][idx[i]] < best_v
        best_v = values[i][idx[i]]
        best_i = i
      end
    end
    ans += best_v * day
    idx[best_i] -= 1
    day += 1
  end
  ans
end
