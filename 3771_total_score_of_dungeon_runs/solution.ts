// LeetCode 3771 - Total Score of Dungeon Runs
// https://leetcode.com/problems/total-score-of-dungeon-runs/

export function totalScore(hp: any, damage: any, requirement: any): any {
    const n = damage.length;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + damage[i];
    let answer = n * (n + 1) / 2;
    for (let j = 1; j <= n; j++) {
        const threshold = prefix[j] + (requirement[j - 1] - hp);
        let lo = 0, hi = j;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (prefix[mid] < threshold) lo = mid + 1;
            else hi = mid;
        }
        answer -= lo;
    }
    return answer;
}
