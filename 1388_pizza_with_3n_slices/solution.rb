# LeetCode 1388 - Pizza With 3N Slices
# https://leetcode.com/problems/pizza-with-3n-slices/

def max_size_slices(slices)
  k = slices.length / 3
  line = lambda do |a|
    dp = Array.new(a.length + 2) { Array.new(k + 1, 0) }
    a.each_with_index do |x, idx|
      i = idx + 2
      (1..k).each do |j|
        dp[i][j] = [dp[i - 1][j], dp[i - 2][j - 1] + x].max
      end
    end
    dp[-1][k]
  end
  [line.call(slices[0...-1]), line.call(slices[1..])].max
end
