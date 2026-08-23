// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

public class Solution {
    public IList<string> FindAllRecipes(string[] recipes, IList<IList<string>> ingredients, string[] supplies) {
        var have = new HashSet<string>(supplies);
        var indeg = new Dictionary<string, int>();
        var graph = new Dictionary<string, List<string>>();
        for (int i = 0; i < recipes.Length; i++) {
            indeg[recipes[i]] = ingredients[i].Count;
            foreach (string ing in ingredients[i]) {
                if (!graph.ContainsKey(ing)) graph[ing] = new List<string>();
                graph[ing].Add(recipes[i]);
            }
        }
        var q = new Queue<string>();
        foreach (string s in have) q.Enqueue(s);
        var ans = new List<string>();
        while (q.Count > 0) {
            string cur = q.Dequeue();
            if (!graph.ContainsKey(cur)) continue;
            foreach (string nxt in graph[cur]) {
                if (--indeg[nxt] == 0) {
                    ans.Add(nxt);
                    q.Enqueue(nxt);
                }
            }
        }
        return ans;
    }
}
