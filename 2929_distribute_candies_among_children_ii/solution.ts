// LeetCode 2929 - Distribute Candies Among Children II
// https://leetcode.com/problems/distribute-candies-among-children-ii/

export function distributeCandies(n: number, limit: number): number {
    const comb2 = (x) => {
        if (x < 0) return 0;
        return (x + 1) * (x + 2) / 2;
    };
    let ans = comb2(n);
    ans -= 3 * comb2(n - (limit + 1));
    ans += 3 * comb2(n - 2 * (limit + 1));
    ans -= comb2(n - 3 * (limit + 1));
    return ans;
}
