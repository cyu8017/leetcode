// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

export function buildWall(height: number, width: number, bricks: number[]): number {
    const MOD = 1000000007;
    const masks = [];
    const gen = (remain, mask) => {
        if (remain === 0) { masks.push(mask); return; }
        for (const b of bricks) {
            if (b <= remain) {
                let nm = mask;
                if (remain - b > 0) nm |= 1 << (remain - b);
                gen(remain - b, nm);
            }
        }
    };
    gen(width, 0);
    const m = masks.length;
    const compat = Array.from({length: m}, () => []);
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < m; j++)
            if ((masks[i] & masks[j]) === 0) compat[i].push(j);
    }
    let dp = new Array(m).fill(1);
    for (let h = 1; h < height; h++) {
        const ndp = new Array(m).fill(0);
        for (let i = 0; i < m; i++)
            for (const j of compat[i]) ndp[j] = (ndp[j] + dp[i]) % MOD;
        dp = ndp;
    }
    let ans = 0;
    for (const v of dp) ans = (ans + v) % MOD;
    return ans;
}
