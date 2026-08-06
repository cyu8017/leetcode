# LeetCode 1452 - People Whose List Of Favorite Companies Is Not A Subset Of Another List
# https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

def people_indexes(favorite_companies)
  sets = favorite_companies.map { |x| x.each_with_object({}) { |c, h| h[c] = true } }
  (0...sets.length).select do |i|
    !(0...sets.length).any? { |j| i != j && sets[i].all? { |k, _| sets[j].key?(k) } }
  end
end
