// LeetCode 2927 - Distribute Candies Among Children III
// https://leetcode.com/problems/distribute-candies-among-children-iii/

export function distributeCandies(n: number, limit: number): number {
    const comb = (x) => {
        if (x < 2) return 0;
        return x * (x - 1) / 2;
    };
    let ans = comb(n + 2);
    ans -= 3 * comb(n - limit + 1);
    ans += 3 * comb(n - 2 * (limit + 1) + 2);
    ans -= comb(n - 3 * (limit + 1) + 2);
    if (ans < 0) ans = 0;
    return ans;
}
