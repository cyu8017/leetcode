// LeetCode 0843 - Guess the Word
// https://leetcode.com/problems/guess-the-word/

export function findSecretWord(words: string[], master: Master): void {
    const match = (a, b) => {
        let m = 0;
        for (let i = 0; i < a.length; i++) if (a[i] === b[i]) m++;
        return m;
    };
    let candidates = words.slice();
    while (candidates.length) {
        let best = candidates[0];
        let bestWorst = candidates.length + 1;
        for (const w of candidates) {
            const buckets = new Array(7).fill(0);
            for (const c of candidates) buckets[match(w, c)]++;
            let worst = 0;
            for (const b of buckets) worst = Math.max(worst, b);
            if (worst < bestWorst) {
                bestWorst = worst;
                best = w;
            }
        }
        const score = master.guess(best);
        if (score === 6) return;
        candidates = candidates.filter(c => match(c, best) === score);
    }
}
