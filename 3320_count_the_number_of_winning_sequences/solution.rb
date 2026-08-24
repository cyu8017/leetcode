# LeetCode 3320 - Count the Number of Winning Sequences
# https://leetcode.com/problems/count-the-number-of-winning-sequences/

# @param {String} s
# @return {Integer}
def count_winning_sequences(s)
  mod = 1_000_000_007
  n = s.length
  mp = { "F" => 0, "W" => 1, "E" => 2 }
  beat = [2, 0, 1]
  score = Array.new(3) { Array.new(3, 0) }
  3.times do |a|
    3.times do |b|
      score[a][b] = if a == b
                      0
                    elsif beat[a] == b
                      1
                    else
                      -1
                    end
    end
  end
  offset = n
  dp = Array.new(3) { Array.new(2 * n + 1, 0) }
  b0 = mp[s[0]]
  3.times { |a| dp[a][score[a][b0] + offset] = 1 }
  (1...n).each do |i|
    ndp = Array.new(3) { Array.new(2 * n + 1, 0) }
    b = mp[s[i]]
    3.times do |last|
      (0..(2 * n)).each do |d|
        next if dp[last][d] == 0

        3.times do |a|
          next if a == last

          nd = d + score[a][b]
          next if nd < 0 || nd > 2 * n

          ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod
        end
      end
    end
    dp = ndp
  end
  ans = 0
  3.times do |a|
    ((offset + 1)..(2 * n)).each { |d| ans = (ans + dp[a][d]) % mod }
  end
  ans
end
