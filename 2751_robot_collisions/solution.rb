# LeetCode 2751 - Robot Collisions
# https://leetcode.com/problems/robot-collisions/

# @param {Integer[]} positions
# @param {Integer[]} healths
# @param {String} directions
# @return {Integer[]}
def survived_robots_healths(positions, healths, directions)
  n = positions.length
  idx = (0...n).to_a.sort_by { |i| positions[i] }
  stack = []
  idx.each do |i|
    if directions[i] == "R"
      stack << i
    else
      while !stack.empty? && directions[stack[-1]] == "R" && healths[i] > 0
        j = stack[-1]
        if healths[j] < healths[i]
          healths[j] = 0
          healths[i] -= 1
          stack.pop
        elsif healths[j] > healths[i]
          healths[j] -= 1
          healths[i] = 0
        else
          healths[j] = 0
          healths[i] = 0
          stack.pop
        end
      end
      stack << i if healths[i] > 0
    end
  end
  (0...n).filter_map { |i| healths[i] if healths[i] > 0 }
end
