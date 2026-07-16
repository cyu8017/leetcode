def num_distinct(s, t)
  dp = Array.new(t.length + 1, 0)
  dp[0] = 1
  s.each_char do |character|
    (t.length - 1).downto(0) do |index|
      dp[index + 1] += dp[index] if character == t[index]
    end
  end
  dp[t.length]
end