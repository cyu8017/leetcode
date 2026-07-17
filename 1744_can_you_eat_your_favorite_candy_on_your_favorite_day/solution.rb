# LeetCode 1744 - Can You Eat Your Favorite Candy on Your Favorite Day?
# https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/

# @param {Integer[]} candies_count
# @param {Integer[][]} queries
# @return {Boolean[]}
def can_eat(candies_count, queries)
  prefix = [0]
  candies_count.each { |count| prefix << prefix[-1] + count }
  queries.map do |candy_type, day, cap|
    min_eaten = day + 1
    max_eaten = (day + 1) * cap
    max_eaten > prefix[candy_type] && min_eaten <= prefix[candy_type + 1]
  end
end
