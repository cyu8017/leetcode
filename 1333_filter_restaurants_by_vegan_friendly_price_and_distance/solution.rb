# LeetCode 1333 - Filter Restaurants By Vegan Friendly Price And Distance
# https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

def filter_restaurants(restaurants, vegan_friendly, max_price, max_distance)
  valid = restaurants.select do |row|
    (vegan_friendly == 0 || row[2] == 1) && row[3] <= max_price && row[4] <= max_distance
  end
  valid.sort_by { |row| [-row[1], -row[0]] }.map(&:first)
end
