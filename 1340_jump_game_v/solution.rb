# LeetCode 1340 - Jump Game V
# https://leetcode.com/problems/jump-game-v/

def max_jumps(arr, d)
  dp = Array.new(arr.length, 1)
  arr.each_with_index.map { |value, i| [value, i] }.sort.each do |_value, i|
    [-1, 1].each do |step|
      j = i + step
      while j >= 0 && j < arr.length && (j - i).abs <= d && arr[j] < arr[i]
        dp[i] = [dp[i], 1 + dp[j]].max
        j += step
      end
    end
  end
  dp.max
end
