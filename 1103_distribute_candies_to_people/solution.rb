# LeetCode 1103 - Distribute Candies to People
# https://leetcode.com/problems/distribute-candies-to-people/

# @param {Integer} candies
# @param {Integer} num_people
# @return {Integer[]}
def distribute_candies(candies, num_people)
  ans = Array.new(num_people, 0)
  give = 1
  i = 0
  while candies > 0
    take = [give, candies].min
    ans[i] += take
    candies -= take
    give += 1
    i = (i + 1) % num_people
  end
  ans
end
