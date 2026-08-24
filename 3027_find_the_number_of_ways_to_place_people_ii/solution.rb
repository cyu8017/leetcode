# LeetCode 3027 - Find the Number of Ways to Place People II
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

# @param {Integer[][]} points
# @return {Integer}
def number_of_pairs(points)
  points.sort_by! { |a| [a[0], -a[1]] }
  ans = 0
  points.length.times do |i|
    y1 = points[i][1]
    max_y = -1 << 60
    (i + 1...points.length).each do |j|
      y2 = points[j][1]
      if max_y < y2 && y2 <= y1
        max_y = y2
        ans += 1
      end
    end
  end
  ans
end
