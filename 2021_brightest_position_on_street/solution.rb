# LeetCode 2021 - Brightest Position on Street
# https://leetcode.com/problems/brightest-position-on-street/

# @param {Integer[][]} lights
# @return {Integer}
def brightest_position(lights)
  events = []
  lights.each do |pos, r|
    events << [pos - r, 1]
    events << [pos + r + 1, -1]
  end
  events.sort_by! { |e| [e[0], e[1]] }
  best = 0
  cur = 0
  ans = 0
  events.each do |pos, d|
    cur += d
    if cur > best
      best = cur
      ans = pos
    end
  end
  ans
end

alias solve brightest_position
