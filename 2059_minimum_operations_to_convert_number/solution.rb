# LeetCode 2059 - Minimum Operations to Convert Number
# https://leetcode.com/problems/minimum-operations-to-convert-number/

# @param {Integer[]} nums
# @param {Integer} start
# @param {Integer} goal
# @return {Integer}
def minimum_operations(nums, start, goal)
  return 0 if start == goal

  vis = { start => true }
  q = [start]
  steps = 0
  until q.empty?
    steps += 1
    q.length.times do
      cur = q.shift
      nums.each do |x|
        [cur + x, cur - x, cur ^ x].each do |nxt|
          return steps if nxt == goal

          if nxt.between?(0, 1000) && !vis[nxt]
            vis[nxt] = true
            q << nxt
          end
        end
      end
    end
  end
  -1
end
