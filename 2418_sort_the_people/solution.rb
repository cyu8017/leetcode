# LeetCode 2418 - Sort the People
# https://leetcode.com/problems/sort-the-people/

# @param {String[]} names
# @param {Integer[]} heights
# @return {String[]}
def sort_people(names, heights)
  n = names.length
  idx = (0...n).to_a
  idx.sort_by! { |i| -heights[i] }
  idx.map { |i| names[i] }
end
