// LeetCode 3926 - Count Valid Word Occurrences
// https://leetcode.com/problems/count-valid-word-occurrences/

export function countWordOccurrences(chunks: any, queries: any): any {
        let sb = "";
        for (const c of chunks) sb+= (c);
        let s = sb;
        let n = s.length;
        let cnt = new Map();
        let i = 0;
        while (i < n) {
            if (s[i] == ' ' || s[i] == '-') {
                i++;
                continue;
            }
            let j = i;
            while (j < n && s[j] != ' ' && (s[j] != '-' || (j + 1 < n && s[j + 1] != ' ' && s[j + 1] != '-'))) {
                j++;
            }
            let word = s.substring(i, j);
            cnt.set(word, (cnt.has(word) ? cnt.get(word) : 0) + 1);
            i = j;
        }
        let ans = new Array(queries.length).fill(0);
        for (let k = 0; k < queries.length; k++) ans[k] = (cnt.has(queries[k]) ? cnt.get(queries[k]) : 0);
        return ans;
    
}
