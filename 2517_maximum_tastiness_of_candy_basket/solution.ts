// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

export function maximumTastiness(price: number[], k: number): number {
    price = price.slice().sort((a, b) => a - b);
    const ok = (d) => {
        let cnt = 1, last = price[0];
        for (let i = 1; i < price.length; i++) {
            if (price[i] - last >= d) {
                cnt++;
                last = price[i];
                if (cnt >= k) return true;
            }
        }
        return false;
    };
    let lo = 0, hi = price[price.length - 1] - price[0];
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (ok(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
