# LeetCode 4001 - Aggregate Two Time Series
# https://leetcode.com/problems/aggregate-two-time-series/

# @param {Integer[][]} series1
# @param {Integer[][]} series2
# @return {Integer[][]}
def aggregate_time_series(series1, series2)
  m = series1.length
  n = series2.length
  i = 0
  j = 0
  ans = []
  while i < m && j < n
    t1, v1 = series1[i][0], series1[i][1]
    t2, v2 = series2[j][0], series2[j][1]
    if t1 == t2
      ans << [t1, v1 + v2]
      i += 1
      j += 1
    elsif t1 < t2
      ans << [t1, v1 + v2]
      i += 1
    else
      ans << [t2, v1 + v2]
      j += 1
    end
  end
  while i < m
    ans << [series1[i][0], series1[i][1]]
    i += 1
  end
  while j < n
    ans << [series2[j][0], series2[j][1]]
    j += 1
  end
  ans
end
