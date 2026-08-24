// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

export function maxWeight(pizzas: any): any {
    pizzas = pizzas.slice().sort((a, b) => a - b);
    const n = pizzas.length;
    const days = Math.floor(n / 4);
    let ans = 0;
    const oddDays = Math.floor((days + 1) / 2);
    const evenDays = Math.floor(days / 2);
    let idx = n - 1;
    for (let i = 0; i < oddDays; i++) {
        ans += pizzas[idx];
        idx--;
    }
    for (let i = 0; i < evenDays; i++) {
        idx--;
        ans += pizzas[idx];
        idx--;
    }
    return ans;
}
