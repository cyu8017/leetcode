# LeetCode 2891 - Method Chaining
# https://leetcode.com/problems/method-chaining/

# @param {Object[]} animals
# @return {Object[]}
def find_heavy_animals(animals)
  weight = lambda { |r| r.is_a?(Array) ? r[3] : r["weight"] }
  filtered = animals.select { |r| weight.call(r) > 100 }
  filtered.sort_by! { |r| -weight.call(r) }
  filtered.map { |r| { "name" => r.is_a?(Array) ? r[0] : r["name"] } }
end
