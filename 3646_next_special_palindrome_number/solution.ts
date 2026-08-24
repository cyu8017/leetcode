// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

export function specialPalindrome(n: any): any {
    const cands = [];
    let halfCnt, mid, halfLen;
    const dfs = (pos, cur) => {
        if (pos === halfLen) {
            const left = cur.join('');
            let s = left;
            if (mid > 0) s += mid;
            for (let i = left.length - 1; i >= 0; i--) s += left[i];
            cands.push(Number(s));
            return;
        }
        for (let d = 1; d <= 9; d++) {
            if (halfCnt[d] === 0) continue;
            halfCnt[d]--;
            cur.push(d);
            dfs(pos + 1, cur);
            cur.pop();
            halfCnt[d]++;
        }
    };
    const gen = (mask) => {
        let total = 0, odd = 0;
        for (let d = 1; d <= 9; d++) {
            if (((mask >> d) & 1) !== 0) {
                total += d;
                if (d % 2 === 1) odd++;
            }
        }
        if (total === 0 || total > 18 || odd > 1) return;
        halfCnt = new Array(10).fill(0);
        mid = 0;
        for (let d = 1; d <= 9; d++) {
            if (((mask >> d) & 1) === 0) continue;
            halfCnt[d] = Math.floor(d / 2);
            if (d % 2 === 1) mid = d;
        }
        halfLen = Math.floor(total / 2);
        dfs(0, []);
    };
    for (let mask = 1; mask < (1 << 10); mask++) {
        if ((mask & 1) !== 0) continue;
        gen(mask);
    }
    cands.sort((a, b) => a - b);
    for (const v of cands)
        if (v > n) return v;
    return -1;
}
