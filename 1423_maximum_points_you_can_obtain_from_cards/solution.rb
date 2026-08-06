# LeetCode 1423 - Maximum Points You Can Obtain From Cards
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

def max_score(card_points, k)
  return card_points.sum if k == card_points.length
  window = card_points.length - k
  current = card_points.first(window).sum
  smallest = current
  (window...card_points.length).each do |i|
    current += card_points[i] - card_points[i - window]
    smallest = [smallest, current].min
  end
  card_points.sum - smallest
end
