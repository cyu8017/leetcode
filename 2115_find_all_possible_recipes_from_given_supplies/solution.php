<?php
// LeetCode 2115 - Find All Possible Recipes from Given Supplies
// https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution {
    /**
     * @param String[] $recipes
     * @param String[][] $ingredients
     * @param String[] $supplies
     * @return String[]
     */
    function findAllRecipes($recipes, $ingredients, $supplies) {
        $have = array_fill_keys($supplies, true);
        $indeg = [];
        $graph = [];
        for ($i = 0; $i < count($recipes); $i++) {
            $indeg[$recipes[$i]] = count($ingredients[$i]);
            foreach ($ingredients[$i] as $ing) {
                if (!isset($graph[$ing])) $graph[$ing] = [];
                $graph[$ing][] = $recipes[$i];
            }
        }
        $q = $supplies;
        $ans = [];
        while ($q) {
            $cur = array_shift($q);
            if (!isset($graph[$cur])) continue;
            foreach ($graph[$cur] as $nxt) {
                $d = $indeg[$nxt] - 1;
                $indeg[$nxt] = $d;
                if ($d === 0) {
                    $ans[] = $nxt;
                    $q[] = $nxt;
                }
            }
        }
        return $ans;
    }
}
