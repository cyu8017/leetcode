// LeetCode 0638 - Shopping Offers
// https://leetcode.com/problems/shopping-offers/

export function shoppingOffers(price: number[], special: number[][], needs: number[]): number {
    const memo = new Map();
    const dfs = (state) => {
        const key = state.join(",");
        if (memo.has(key)) return memo.get(key);
        let cost = 0;
        for (let i = 0; i < price.length; ++i) cost += state[i] * price[i];
        for (const offer of special) {
            const nxt = state.slice();
            let valid = true;
            for (let i = 0; i < price.length; ++i) {
                if (nxt[i] < offer[i]) { valid = false; break; }
                nxt[i] -= offer[i];
            }
            if (valid) cost = Math.min(cost, offer[price.length] + dfs(nxt));
        }
        memo.set(key, cost);
        return cost;
    };
    return dfs(needs.slice());
}
