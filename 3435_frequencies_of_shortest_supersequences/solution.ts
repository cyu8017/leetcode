// LeetCode 3435 - Frequencies of Shortest Supersequences
// https://leetcode.com/problems/frequencies-of-shortest-supersequences/

export function supersequences(words: any): any {
    const used = new Array(26).fill(false);
    for (const w of words) {
        used[w.charCodeAt(0) - 97] = true;
        used[w.charCodeAt(1) - 97] = true;
    }
    const letters = [];
    for (let i = 0; i < 26; i++) if (used[i]) letters.push(i);
    const m = letters.length;
    const freq = new Array(26).fill(0);
    let best = 1e9;
    let bestFreqs = [];
    const dfs = (i) => {
        if (i === m) {
            for (const w of words) {
                const a = w.charCodeAt(0) - 97, b = w.charCodeAt(1) - 97;
                if (a === b) {
                    if (freq[a] < 2) return;
                } else if (freq[a] < 1 || freq[b] < 1) return;
            }
            let sum = 0;
            const f = freq.slice();
            for (let j = 0; j < 26; j++) sum += freq[j];
            if (sum < best) {
                best = sum;
                bestFreqs = [f];
            } else if (sum === best) bestFreqs.push(f);
            return;
        }
        const L = letters[i];
        for (let c = 1; c <= 2; c++) {
            freq[L] = c;
            dfs(i + 1);
        }
        freq[L] = 0;
    };
    dfs(0);
    return bestFreqs;
}
