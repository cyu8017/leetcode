# LeetCode 0825 - Friends Of Appropriate Ages
# https://leetcode.com/problems/friends-of-appropriate-ages/

# @param {Integer[]} ages
# @return {Integer}
def num_friend_requests(ages)
  count = Array.new(121, 0)
  ages.each { |age| count[age] += 1 }
  ans = 0
  (1..120).each do |x|
    next if count[x] == 0

    (1..120).each do |y|
      next if count[y] == 0
      next if y <= 0.5 * x + 7 || y > x || (y > 100 && x < 100)

      ans += count[x] * count[y]
      ans -= count[x] if x == y
    end
  end
  ans
end
