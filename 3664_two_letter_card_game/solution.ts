// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

export function score(cards: any, x: any): any {
    const pairGroup = (arr) => {
        let total = 0, mx = 0;
        for (let i = 0; i < 26; i++) {
            total += arr[i];
            mx = Math.max(mx, arr[i]);
        }
        let pairs = Math.floor(total / 2);
        if (total - mx < pairs) pairs = total - mx;
        return [pairs, total - 2 * pairs];
    };
    let xx = 0;
    const left = new Array(26).fill(0), right = new Array(26).fill(0);
    for (const c of cards) {
        const a = c[0], b = c[1];
        if (a === x && b === x) xx++;
        else if (a === x) left[b.charCodeAt(0) - 97]++;
        else if (b === x) right[a.charCodeAt(0) - 97]++;
    }
    const lp = pairGroup(left), rp = pairGroup(right);
    let ans = lp[0] + rp[0];
    const rem = lp[1] + rp[1];
    const use = Math.min(xx, rem);
    ans += use;
    xx -= use;
    ans += Math.floor(xx / 2);
    return ans;
}
