# LeetCode 1431 - Kids With The Greatest Number Of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kids_with_candies(candies, extra_candies)
  maximum = candies.max
  candies.map { |value| value + extra_candies >= maximum }
end
