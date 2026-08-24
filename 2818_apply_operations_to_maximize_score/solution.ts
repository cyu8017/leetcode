// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

export function maximumScore(nums: number[], k: number): number {
    const MOD = 1000000007n;
    const n = nums.length;
    let maxV = 0;
    for (const v of nums) maxV = Math.max(maxV, v);
    const spf = Array(maxV + 1).fill(0);
    for (let i = 2; i <= maxV; i++) {
        if (spf[i] === 0) {
            for (let j = i; j <= maxV; j += i) if (spf[j] === 0) spf[j] = i;
        }
    }
    const primeScore = (x) => {
        const seen = new Set();
        while (x > 1) {
            const p = spf[x];
            seen.add(p);
            while (x % p === 0) x = Math.floor(x / p);
        }
        return seen.size;
    };
    const score = nums.map(primeScore);
    const left = Array(n), right = Array(n);
    const st = [];
    for (let i = 0; i < n; i++) {
        while (st.length && score[st[st.length - 1]] < score[i]) st.pop();
        left[i] = st.length ? st[st.length - 1] : -1;
        st.push(i);
    }
    st.length = 0;
    for (let i = n - 1; i >= 0; i--) {
        while (st.length && score[st[st.length - 1]] <= score[i]) st.pop();
        right[i] = st.length ? st[st.length - 1] : n;
        st.push(i);
    }
    const arr = Array.from({length: n}, (_, i) => [nums[i], (i - left[i]) * (right[i] - i)]);
    arr.sort((a, b) => b[0] - a[0]);
    const modPow = (a, b) => {
        let res = 1n, base = BigInt(a) % MOD, exp = BigInt(b);
        while (exp > 0n) {
            if (exp & 1n) res = res * base % MOD;
            base = base * base % MOD;
            exp >>= 1n;
        }
        return res;
    };
    let ans = 1n;
    let remain = BigInt(k);
    for (const [val, cnt] of arr) {
        if (remain <= 0n) break;
        const use = cnt < remain ? BigInt(cnt) : remain;
        ans = ans * modPow(val, use) % MOD;
        remain -= use;
    }
    return Number(ans);
}
