# LeetCode 3680 - Generate Schedule
# https://leetcode.com/problems/generate-schedule/

# @param {Integer} n
# @return {Integer[][]}
def generate_schedule(n)
  return [] if n < 5

  matches = []
  (0...n).each do |i|
    (0...n).each { |j| matches << [i, j] if i != j }
  end
  used = Array.new(matches.length, false)
  sched = []
  last = [-1, -1]
  dfs = nil
  dfs = lambda do
    return true if sched.length == matches.length

    matches.each_with_index do |m, i|
      next if used[i]
      next if m[0] == last[0] || m[0] == last[1] || m[1] == last[0] || m[1] == last[1]

      used[i] = true
      sched << m
      p0 = last[0]
      p1 = last[1]
      last[0] = m[0]
      last[1] = m[1]
      return true if dfs.call

      last[0] = p0
      last[1] = p1
      sched.pop
      used[i] = false
    end
    false
  end
  return sched if dfs.call

  []
end
