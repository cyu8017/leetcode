// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

export function maxPrice(items: number[][], capacity: number): number {
    items.sort((a, b) => b[0] / b[1] - a[0] / a[1]);
    let ans = 0.0, remain = capacity;
    for (const it of items) {
        const price = it[0], weight = it[1];
        if (remain >= weight) {
            ans += price;
            remain -= weight;
        } else {
            ans += price * remain / weight;
            remain = 0;
            break;
        }
    }
    if (remain > 0) return -1;
    return ans;
}
