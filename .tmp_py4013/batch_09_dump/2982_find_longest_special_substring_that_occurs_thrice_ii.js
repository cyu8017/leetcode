// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

var maximumLength = function(s) {
    const groups = Array.from({length: 26}, () => []);
    const n = s.length;
    for (let i = 0; i < n; ) {
        let j = i;
        while (j < n && s[j] === s[i]) j++;
        groups[s.charCodeAt(i) - 97].push(j - i);
        i = j;
    }
    let ans = -1;
    for (let c = 0; c < 26; c++) {
        const arr = groups[c];
        if (!arr.length) continue;
        arr.sort((a, b) => b - a);
        for (let L = arr[0]; L >= 1; L--) {
            let cnt = 0;
            for (const g of arr) {
                if (g >= L) cnt += g - L + 1;
            }
            if (cnt >= 3) {
                if (L > ans) ans = L;
                break;
            }
        }
    }
    return ans;
};
