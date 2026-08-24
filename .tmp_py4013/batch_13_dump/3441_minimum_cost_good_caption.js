// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

var minCostGoodCaption = function(caption) {
    const n = caption.length;
    if (n < 3) return "";
    const ans = caption.split("");
    let i = 0;
    while (i < n) {
        let j = i;
        while (j < n && ans[j] === ans[i]) j++;
        if (j - i >= 3) { i = j; continue; }
        const need = 3 - (j - i);
        if (j + need <= n) {
            for (let t = 0; t < need; t++) ans[j + t] = ans[i];
            i = j + need;
        } else {
            let ch = "a";
            if (i > 0) ch = ans[i - 1];
            else if (j < n) ch = caption[j];
            for (let t = i; t < n; t++) ans[t] = ch;
            break;
        }
    }
    i = 0;
    while (i < n) {
        let j = i;
        while (j < n && ans[j] === ans[i]) j++;
        if (j - i < 3) return "";
        i = j;
    }
    return ans.join("");
};
