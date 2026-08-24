// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

export function maximumBeauty(items: number[][], queries: number[]): number[] {
    items.sort((a, b) => a[0] - b[0]);
    let maxB = 0;
    for (const it of items) {
        maxB = Math.max(maxB, it[1]);
        it[1] = maxB;
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        let lo = 0, hi = items.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (items[mid][0] <= queries[i]) lo = mid + 1;
            else hi = mid;
        }
        ans[i] = lo === 0 ? 0 : items[lo - 1][1];
    }
    return ans;
}
