# LeetCode 3704 - Count No-Zero Pairs That Sum to N
# https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

# @param {Integer} n
# @return {Integer}
def count_no_zero_pairs(n)
  s = n.to_s
  m = s.length
  digits = Array.new(m + 1, 0)
  (0...m).each { |i| digits[i] = s[m - 1 - i].ord - 48 }
  dp = Array.new(2) { Array.new(2) { Array.new(2, 0) } }
  dp[0][1][1] = 1
  (0..m).each do |pos|
    ndp = Array.new(2) { Array.new(2) { Array.new(2, 0) } }
    target = digits[pos]
    (0...2).each do |carry|
      (0...2).each do |alive_a|
        (0...2).each do |alive_b|
          ways = dp[carry][alive_a][alive_b]
          next if ways == 0

          a_opts = []
          if alive_a == 1
            (1..9).each { |d| a_opts << [d, 1] }
            a_opts << [0, 0] if pos > 0
          else
            a_opts << [0, 0]
          end
          b_opts = []
          if alive_b == 1
            (1..9).each { |d| b_opts << [d, 1] }
            b_opts << [0, 0] if pos > 0
          else
            b_opts << [0, 0]
          end
          a_opts.each do |da, na|
            b_opts.each do |db, nb|
              sm = da + db + carry
              next if sm % 10 != target

              ncarry = sm / 10
              ndp[ncarry][na][nb] += ways
            end
          end
        end
      end
    end
    dp = ndp
  end
  dp[0][0][0]
end
