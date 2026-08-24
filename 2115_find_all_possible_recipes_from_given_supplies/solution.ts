// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

export function findAllRecipes(recipes: string[], ingredients: string[][], supplies: string[]): string[] {
    const have = new Set(supplies);
    const indeg = new Map();
    const graph = new Map();
    for (let i = 0; i < recipes.length; i++) {
        indeg.set(recipes[i], ingredients[i].length);
        for (const ing of ingredients[i]) {
            if (!graph.has(ing)) graph.set(ing, []);
            graph.get(ing).push(recipes[i]);
        }
    }
    const q = [...have];
    const ans = [];
    while (q.length) {
        const cur = q.shift();
        if (!graph.has(cur)) continue;
        for (const nxt of graph.get(cur)) {
            const d = indeg.get(nxt) - 1;
            indeg.set(nxt, d);
            if (d === 0) {
                ans.push(nxt);
                q.push(nxt);
            }
        }
    }
    return ans;
}
