class Solution
  def candy(ratings)
    candies = Array.new(ratings.length, 1)
    (1...ratings.length).each do |i|
      candies[i] = candies[i - 1] + 1 if ratings[i] > ratings[i - 1]
    end
    (ratings.length - 2).downto(0) do |i|
      candies[i] = [candies[i], candies[i + 1] + 1].max if ratings[i] > ratings[i + 1]
    end
    candies.sum
  end
end