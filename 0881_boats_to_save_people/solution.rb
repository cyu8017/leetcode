# LeetCode 0881 - Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/

# @param {Integer[]} people
# @param {Integer} limit
# @return {Integer}
def num_rescue_boats(people, limit)
  people.sort!
  i = 0
  j = people.length - 1
  boats = 0
  while i <= j
    i += 1 if people[i] + people[j] <= limit
    j -= 1
    boats += 1
  end
  boats
end
