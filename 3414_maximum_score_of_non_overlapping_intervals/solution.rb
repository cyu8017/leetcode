# LeetCode 3414 - Maximum Score of Non-overlapping Intervals
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

# @param {Integer[][]} intervals
# @return {Integer[]}
def maximum_weight(intervals)
  n = intervals.length
  arr = intervals.each_with_index.map { |it, i| { l: it[0], r: it[1], w: it[2], i: i } }
  arr.sort_by! { |a| a[:r] }
  dp = Array.new(n + 1) { Array.new(5) { { score: 0, idx: [] } } }
  (1..n).each do |i|
    cur = arr[i - 1]
    (0...5).each { |t| dp[i][t] = copy_state_3414(dp[i - 1][t]) }
    lo = 0
    hi = i - 1
    while lo < hi
      mid = (lo + hi) / 2
      if arr[mid][:r] < cur[:l]
        lo = mid + 1
      else
        hi = mid
      end
    end
    prev = lo
    (1...5).each do |t|
      prev_state = dp[prev][t - 1]
      cand = copy_state_3414(prev_state)
      cand[:score] = prev_state[:score] + cur[:w]
      cand[:idx] << cur[:i]
      cand[:idx].sort!
      dp[i][t] = better_3414(dp[i][t], cand)
    end
  end
  best = dp[n][0]
  (1...5).each { |t| best = better_3414(best, dp[n][t]) }
  best[:idx]
end

def copy_state_3414(s)
  { score: s[:score], idx: s[:idx].dup }
end

def better_3414(a, b)
  return a[:score] > b[:score] ? a : b if a[:score] != b[:score]

  m = [a[:idx].length, b[:idx].length].min
  (0...m).each do |i|
    return a[:idx][i] < b[:idx][i] ? a : b if a[:idx][i] != b[:idx][i]
  end
  a[:idx].length <= b[:idx].length ? a : b
end
