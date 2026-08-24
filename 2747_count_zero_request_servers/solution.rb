# LeetCode 2747 - Count Zero Request Servers
# https://leetcode.com/problems/count-zero-request-servers/

# @param {Integer} n
# @param {Integer[][]} logs
# @param {Integer} x
# @param {Integer[]} queries
# @return {Integer[]}
def count_servers(n, logs, x, queries)
  logs = logs.sort_by { |e| e[1] }
  qs = queries.each_with_index.map { |t, i| [t, i] }.sort_by { |t, _| t }
  freq = Hash.new(0)
  active = 0
  ans = Array.new(queries.length, 0)
  l = 0
  r = 0
  m = logs.length
  qs.each do |t, qi|
    while r < m && logs[r][1] <= t
      sid = logs[r][0]
      freq[sid] += 1
      active += 1 if freq[sid] == 1
      r += 1
    end
    while l < r && logs[l][1] < t - x
      sid = logs[l][0]
      freq[sid] -= 1
      active -= 1 if freq[sid] == 0
      l += 1
    end
    ans[qi] = n - active
  end
  ans
end
