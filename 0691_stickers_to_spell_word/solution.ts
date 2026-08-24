// LeetCode 0691 - Stickers to Spell Word
// https://leetcode.com/problems/stickers-to-spell-word/

export function minStickers(stickers: string[], target: string): number {
    const need = new Array(26).fill(0);
    for (const ch of target) need[ch.charCodeAt(0) - 97]++;
    const chars = [];
    for (let i = 0; i < 26; i++) if (need[i] > 0) chars.push(String.fromCharCode(97 + i));
    const sticks = [];
    for (const sticker of stickers) {
        const counts = new Array(26).fill(0);
        for (const ch of sticker) counts[ch.charCodeAt(0) - 97]++;
        let useful = false;
        for (const ch of chars) if (counts[ch.charCodeAt(0) - 97] > 0) { useful = true; break; }
        if (useful) sticks.push(counts);
    }
    const memo = new Map();
    const key = (state) => state.join(',');
    const dfs = (state) => {
        const k = key(state);
        if (memo.has(k)) return memo.get(k);
        let i = 0;
        while (i < state.length && state[i] === 0) i++;
        if (i === state.length) {
            memo.set(k, 0);
            return 0;
        }
        const first = chars[i];
        let best = 1e9;
        for (const stick of sticks) {
            if (stick[first.charCodeAt(0) - 97] === 0) continue;
            const nxt = state.slice();
            for (let j = 0; j < chars.length; j++) {
                nxt[j] = Math.max(0, nxt[j] - stick[chars[j].charCodeAt(0) - 97]);
            }
            best = Math.min(best, 1 + dfs(nxt));
        }
        memo.set(k, best);
        return best;
    };
    const state = chars.map((ch) => need[ch.charCodeAt(0) - 97]);
    const result = dfs(state);
    return result >= 1e9 ? -1 : result;
}
