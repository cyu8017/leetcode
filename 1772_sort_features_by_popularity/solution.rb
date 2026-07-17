# LeetCode 1772 - Sort Features by Popularity
# https://leetcode.com/problems/sort-features-by-popularity/

# @param {String[]} features
# @param {String[]} responses
# @return {String[]}
def sort_features(features, responses)
  feature_set = {}
  features.each { |f| feature_set[f] = true }
  count = Hash.new(0)
  responses.each do |response|
    seen = {}
    response.split.each do |word|
      seen[word] = true if feature_set.key?(word)
    end
    seen.each_key { |word| count[word] += 1 }
  end
  features.sort_by { |f| [-count[f], f] }
end
