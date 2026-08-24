# LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

# @param {Integer[]} candidates
# @return {Integer}
def largest_combination(candidates)
  ans = 0
  24.times do |bit|
    cnt = 0
    candidates.each { |x| cnt += 1 if ((x >> bit) & 1) == 1 }
    ans = [ans, cnt].max
  end
  ans
end
