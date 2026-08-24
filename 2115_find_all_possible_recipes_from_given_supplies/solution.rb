# LeetCode 2115 - Find All Possible Recipes from Given Supplies
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

# @param {String[]} recipes
# @param {String[][]} ingredients
# @param {String[]} supplies
# @return {String[]}
def find_all_recipes(recipes, ingredients, supplies)
  have = {}
  supplies.each { |s| have[s] = true }
  indeg = {}
  graph = Hash.new { |h, k| h[k] = [] }
  recipes.each_with_index do |r, i|
    indeg[r] = ingredients[i].length
    ingredients[i].each { |ing| graph[ing] << r }
  end
  q = supplies.dup
  ans = []
  until q.empty?
    cur = q.shift
    next unless graph.key?(cur)

    graph[cur].each do |nxt|
      indeg[nxt] -= 1
      if indeg[nxt] == 0
        ans << nxt
        q << nxt
      end
    end
  end
  ans
end
