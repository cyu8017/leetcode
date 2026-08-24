// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

export function generateString(str1: any, str2: any): any {
    const n = str1.length, m = str2.length;
    const L = n + m - 1;
    const ans = new Array(L).fill("?");
    for (let i = 0; i < n; i++) {
        if (str1[i] === "T") {
            for (let j = 0; j < m; j++) {
                if (ans[i + j] !== "?" && ans[i + j] !== str2[j]) return "";
                ans[i + j] = str2[j];
            }
        }
    }
    for (let i = 0; i < L; i++) if (ans[i] === "?") ans[i] = "a";
    for (let i = 0; i < n; i++) {
        if (str1[i] === "F") {
            let match = true;
            for (let j = 0; j < m; j++) if (ans[i + j] !== str2[j]) { match = false; break; }
            if (match) {
                let changed = false;
                for (let j = m - 1; j >= 0; j--) {
                    const pos = i + j;
                    let forced = false;
                    for (let t = 0; t < n; t++) {
                        if (str1[t] === "T" && pos >= t && pos < t + m) { forced = true; break; }
                    }
                    if (!forced) {
                        ans[pos] = "b";
                        changed = true;
                        break;
                    }
                }
                if (!changed) return "";
            }
        }
    }
    for (let i = 0; i < n; i++) {
        let match = true;
        for (let j = 0; j < m; j++) if (ans[i + j] !== str2[j]) { match = false; break; }
        if (str1[i] === "T" && !match) return "";
        if (str1[i] === "F" && match) return "";
    }
    return ans.join("");
}
