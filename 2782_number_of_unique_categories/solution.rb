# LeetCode 2782 - Number of Unique Categories
# https://leetcode.com/problems/number-of-unique-categories/

class CategoryHandler
  def initialize(cats)
    @cats = cats
  end

  def haveSameCategory(a, b)
    @cats[a] == @cats[b]
  end
end

# @param {Integer} n
# @param {Object} category_handler
# @return {Integer}
def number_of_categories(n, category_handler)
  category_handler = CategoryHandler.new(category_handler) if category_handler.is_a?(Array)
  parent = (0...n).to_a
  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      if category_handler.haveSameCategory(i, j)
        a = find.call(i)
        b = find.call(j)
        parent[a] = b if a != b
      end
    end
  end
  (0...n).count { |i| find.call(i) == i }
end
