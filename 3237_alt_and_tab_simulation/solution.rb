# LeetCode 3237 - Alt and Tab Simulation
# https://leetcode.com/problems/alt-and-tab-simulation/

# @param {Integer[]} windows
# @param {Integer[]} queries
# @return {Integer[]}
def simulation_result(windows, queries)
  n = windows.length
  s = Array.new(n + 1, false)
  ans = []
  (queries.length - 1).downto(0) do |i|
    q = queries[i]
    unless s[q]
      s[q] = true
      ans << q
    end
  end
  windows.each { |w| ans << w unless s[w] }
  ans
end
