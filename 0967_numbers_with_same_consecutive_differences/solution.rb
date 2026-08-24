# LeetCode 0967 - Numbers With Same Consecutive Differences
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def nums_same_consec_diff(n, k)
  ans = []
  dfs = lambda do |num, length|
    if length == n
      ans << num
      return
    end
    last = num % 10
    [last - k, last + k].uniq.each do |nxt|
      dfs.call(num * 10 + nxt, length + 1) if nxt >= 0 && nxt <= 9
    end
  end
  (1..9).each { |start| dfs.call(start, 1) }
  ans
end
