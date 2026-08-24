# LeetCode 2211 - Count Collisions on a Road
# https://leetcode.com/problems/count-collisions-on-a-road/

# @param {String} directions
# @return {Integer}
def count_collisions(directions)
  i = 0
  j = directions.length - 1
  i += 1 while i < directions.length && directions[i] == "L"
  j -= 1 while j >= 0 && directions[j] == "R"
  ans = 0
  (i..j).each { |k| ans += 1 if directions[k] != "S" }
  ans
end
