// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

export function stoneGameIX(stones: number[]): boolean {
    const cnt = [0, 0, 0];
    for (const s of stones) cnt[s % 3]++;
    if (cnt[0] % 2 === 0) return cnt[1] > 0 && cnt[2] > 0;
    return Math.abs(cnt[1] - cnt[2]) > 2;
}
