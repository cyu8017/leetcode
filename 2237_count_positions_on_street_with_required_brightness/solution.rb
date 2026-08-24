# LeetCode 2237 - Count Positions on Street With Required Brightness
# https://leetcode.com/problems/count-positions-on-street-with-required-brightness/

# @param {Integer} n
# @param {Integer[][]} lights
# @param {Integer[]} requirement
# @return {Integer}
def meet_requirement(n, lights, requirement)
  diff = Array.new(n + 1, 0)
  lights.each do |pos, r|
    l = [0, pos - r].max
    rr = [n - 1, pos + r].min
    diff[l] += 1
    diff[rr + 1] -= 1
  end
  ans = cur = 0
  n.times do |i|
    cur += diff[i]
    ans += 1 if cur >= requirement[i]
  end
  ans
end

alias solve meet_requirement
