# LeetCode 2353 - Design a Food Rating System
# https://leetcode.com/problems/design-a-food-rating-system/

class FoodRatings
  def initialize(foods, cuisines, ratings)
    @cuisine_of = {}
    @rating_of = {}
    @heaps = {}
    foods.each_index do |i|
      @cuisine_of[foods[i]] = cuisines[i]
      @rating_of[foods[i]] = ratings[i]
      @heaps[cuisines[i]] ||= []
      @heaps[cuisines[i]] << foods[i]
    end
  end

  def change_rating(food, new_rating)
    @rating_of[food] = new_rating
    nil
  end

  def highest_rated(cuisine)
    foods = @heaps[cuisine]
    foods.sort_by! { |x| [-@rating_of[x], x] }
    foods[0]
  end
end
