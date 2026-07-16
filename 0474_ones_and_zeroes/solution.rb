# LeetCode 0474 - Ones and Zeroes
# https://leetcode.com/problems/ones-and-zeroes/

class Solution
  def find_max_form(strs, m, n)
    dp = Array.new(m + 1) { Array.new(n + 1, 0) }
    strs.each do |string|
      zeros = string.count("0")
      ones = string.count("1")
      m.downto(zeros) do |zero|
        n.downto(ones) do |one|
          dp[zero][one] = [dp[zero][one], dp[zero - zeros][one - ones] + 1].max
        end
      end
    end
    dp[m][n]
  end

  alias_method :findMaxForm, :find_max_form
end
