# LeetCode 1092 - Shortest Common Supersequence
# https://leetcode.com/problems/shortest-common-supersequence/

# @param {String} str1
# @param {String} str2
# @return {String}
def shortest_common_supersequence(str1, str2)
  m = str1.length
  n = str2.length
  dp = Array.new(m + 1) { Array.new(n + 1, 0) }
  (1..m).each do |i|
    (1..n).each do |j|
      dp[i][j] = if str1[i - 1] == str2[j - 1]
                   dp[i - 1][j - 1] + 1
                 else
                   [dp[i - 1][j], dp[i][j - 1]].max
                 end
    end
  end
  i = m
  j = n
  chars = []
  while i.positive? && j.positive?
    if str1[i - 1] == str2[j - 1]
      chars << str1[i - 1]
      i -= 1
      j -= 1
    elsif dp[i - 1][j] >= dp[i][j - 1]
      chars << str1[i - 1]
      i -= 1
    else
      chars << str2[j - 1]
      j -= 1
    end
  end
  while i.positive?
    chars << str1[i - 1]
    i -= 1
  end
  while j.positive?
    chars << str2[j - 1]
    j -= 1
  end
  chars.reverse.join
end
