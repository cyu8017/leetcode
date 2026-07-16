def minimum_total(triangle)
  dp = triangle[-1].dup
  (triangle.length - 2).downto(0) do |row_index|
    triangle[row_index].each_index do |index|
      dp[index] = triangle[row_index][index] + [dp[index], dp[index + 1]].min
    end
  end
  dp[0]
end