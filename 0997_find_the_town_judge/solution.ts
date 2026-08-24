// LeetCode 0997 - Find the Town Judge
// https://leetcode.com/problems/find-the-town-judge/

export function findJudge(n: number, trust: number[][]): number {
    const score = new Array(n + 1).fill(0);
    for (const t of trust) {
        score[t[0]]--;
        score[t[1]]++;
    }
    for (let i = 1; i <= n; i++) if (score[i] === n - 1) return i;
    return -1;
}
