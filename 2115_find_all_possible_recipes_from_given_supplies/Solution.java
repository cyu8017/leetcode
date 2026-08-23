// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

import java.util.*;

class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        Set<String> have = new HashSet<>(Arrays.asList(supplies));
        Map<String, Integer> indeg = new HashMap<>();
        Map<String, List<String>> graph = new HashMap<>();
        for (int i = 0; i < recipes.length; i++) {
            indeg.put(recipes[i], ingredients.get(i).size());
            for (String ing : ingredients.get(i)) {
                graph.computeIfAbsent(ing, k -> new ArrayList<>()).add(recipes[i]);
            }
        }
        ArrayDeque<String> q = new ArrayDeque<>(have);
        List<String> ans = new ArrayList<>();
        while (!q.isEmpty()) {
            String cur = q.poll();
            if (!graph.containsKey(cur)) continue;
            for (String nxt : graph.get(cur)) {
                if (indeg.merge(nxt, -1, Integer::sum) == 0) {
                    ans.add(nxt);
                    q.offer(nxt);
                }
            }
        }
        return ans;
    }
}
