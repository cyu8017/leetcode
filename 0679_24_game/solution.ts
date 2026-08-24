// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

export function judgePoint24(cards: number[]): boolean {
    const EPS = 1e-6;
    const dfs = (nums) => {
        if (nums.length === 1) return Math.abs(nums[0] - 24) < EPS;
        for (let i = 0; i < nums.length; ++i) {
            for (let j = 0; j < nums.length; ++j) {
                if (i === j) continue;
                const rest = [];
                for (let k = 0; k < nums.length; ++k) {
                    if (k !== i && k !== j) rest.push(nums[k]);
                }
                const a = nums[i], b = nums[j];
                const candidates = [a + b, a - b, a * b];
                if (Math.abs(b) > EPS) candidates.push(a / b);
                for (const value of candidates) {
                    rest.push(value);
                    if (dfs(rest)) return true;
                    rest.pop();
                }
            }
        }
        return false;
    };
    return dfs(cards.map((c) => c * 1.0));
}
