// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution {
    func findAllRecipes(_ recipes: [String], _ ingredients: [[String]], _ supplies: [String]) -> [String] {
        var have = Set(supplies)
        var indeg = [String: Int]()
        var graph = [String: [String]]()
        for i in 0..<recipes.count {
            indeg[recipes[i]] = ingredients[i].count
            for ing in ingredients[i] {
                graph[ing, default: []].append(recipes[i])
            }
        }
        var q = Array(have)
        var head = 0
        var ans = [String]()
        while head < q.count {
            let cur = q[head]; head += 1
            for nxt in graph[cur, default: []] {
                indeg[nxt]! -= 1
                if indeg[nxt] == 0 {
                    ans.append(nxt)
                    q.append(nxt)
                }
            }
        }
        return ans
    }
}
