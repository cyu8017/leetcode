# LeetCode 3363 - Find the Maximum Number of Fruits Collected
# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

# @param {Integer[][]} fruits
# @return {Integer}
def max_collected_fruits(fruits)
  n = fruits.length
  ans = 0
  n.times do |i|
    ans += fruits[i][i]
    fruits[i][i] = 0
  end
  neg = -(1 << 30)
  dp2 = Array.new(n) { Array.new(n, neg) }
  dp3 = Array.new(n) { Array.new(n, neg) }
  dp2[0][n - 1] = fruits[0][n - 1]
  n.times do |i|
    n.times do |j|
      next if dp2[i][j] == neg

      [-1, 0, 1].each do |dj|
        ni = i + 1
        nj = j + dj
        next unless ni < n && nj >= 0 && nj < n && nj > ni

        v = dp2[i][j] + fruits[ni][nj]
        dp2[ni][nj] = v if v > dp2[ni][nj]
      end
    end
  end
  dp3[n - 1][0] = fruits[n - 1][0]
  n.times do |j|
    n.times do |i|
      next if dp3[i][j] == neg

      [-1, 0, 1].each do |di|
        ni = i + di
        nj = j + 1
        next unless ni >= 0 && ni < n && nj < n && ni > nj

        v = dp3[i][j] + fruits[ni][nj]
        dp3[ni][nj] = v if v > dp3[ni][nj]
      end
    end
  end
  ans + dp2[n - 1][n - 1] + dp3[n - 1][n - 1]
end
