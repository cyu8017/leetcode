# LeetCode 2015 - Average Height of Buildings in Each Segment
# https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

# @param {Integer[][]} buildings
# @return {Integer[][]}
def average_height_of_buildings(buildings)
  events = []
  buildings.each do |left, right, h|
    events << [left, 1, h]
    events << [right, -1, h]
  end
  events.sort_by! { |e| [e[0], e[1]] }
  ans = []
  count = 0
  total = 0
  prev = events[0][0]
  events.each do |pos, typ, h|
    if pos != prev && count > 0
      avg = total / count
      if !ans.empty? && ans[-1][1] == prev && ans[-1][2] == avg
        ans[-1][1] = pos
      else
        ans << [prev, pos, avg]
      end
    end
    count += typ
    total += typ * h
    prev = pos
  end
  ans
end

alias solve average_height_of_buildings
