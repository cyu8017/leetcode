// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    private List<Integer> price;
    private List<List<Integer>> special;
    private final Map<List<Integer>, Integer> memo = new HashMap<>();

    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        this.price = price;
        this.special = special;
        memo.clear();
        return dfs(new ArrayList<>(needs));
    }

    private int dfs(List<Integer> state) {
        Integer cached = memo.get(state);
        if (cached != null) {
            return cached;
        }
        int cost = 0;
        for (int i = 0; i < price.size(); ++i) {
            cost += state.get(i) * price.get(i);
        }
        for (List<Integer> offer : special) {
            List<Integer> nxt = new ArrayList<>(state);
            boolean valid = true;
            for (int i = 0; i < price.size(); ++i) {
                if (nxt.get(i) < offer.get(i)) {
                    valid = false;
                    break;
                }
                nxt.set(i, nxt.get(i) - offer.get(i));
            }
            if (valid) {
                cost = Math.min(cost, offer.get(price.size()) + dfs(nxt));
            }
        }
        memo.put(state, cost);
        return cost;
    }
}
