// LeetCode 3799 - Word Squares Ii
// https://leetcode.com/problems/word-squares-ii/

export function wordSquares(words: any): any {
    words = words.slice().sort();
    const n = words.length;
    const ans = [];
    for (let i = 0; i < n; i++) {
        const top = words[i];
        for (let j = 0; j < n; j++) {
            if (j === i) continue;
            const left = words[j];
            for (let k = 0; k < n; k++) {
                if (k === j || k === i) continue;
                const right = words[k];
                for (let h = 0; h < n; h++) {
                    if (h === k || h === j || h === i) continue;
                    const bottom = words[h];
                    if (top[0] === left[0] && top[3] === right[0] &&
                        bottom[0] === left[3] && bottom[3] === right[3]) {
                        ans.push([top, left, right, bottom]);
                    }
                }
            }
        }
    }
    return ans;
}
