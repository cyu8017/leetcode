// LeetCode 3006 - Find Beautiful Indices in the Given Array I
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

function buildLPS(lps, pattern) {
    let l = 0, i = 1;
    const s_l = pattern.length;
    lps[0] = 0;
    while (i < s_l) {
        if (pattern[i] === pattern[l]) {
            l++;
            lps[i] = l;
            i++;
        } else if (l !== 0) {
            l = lps[l - 1];
        } else {
            lps[i] = l;
            i++;
        }
    }
}
function kmp(s, pat, lps, index) {
    const s_len = s.length, pat_l = pat.length;
    let i = 0, j = 0;
    while (s_len - i >= pat_l - j) {
        if (s[i] === pat[j]) {
            i++;
            j++;
        }
        if (j === pat_l) {
            index.push(i - pat_l);
            j = lps[j - 1];
        } else if (i < s_len && s[i] !== pat[j]) {
            if (j !== 0) j = lps[j - 1];
            else i++;
        }
    }
}

var beautifulIndices = function(s, a, b, k) {
    const a_len = a.length, b_len = b.length;
    const lps_a = new Array(a_len), lps_b = new Array(b_len);
    const a_index = [], b_index = [], result = [];
    buildLPS(lps_a, a);
    buildLPS(lps_b, b);
    kmp(s, a, lps_a, a_index);
    kmp(s, b, lps_b, b_index);
    let i = 0, j = 0;
    while (i < a_index.length && j < b_index.length) {
        if (a_index[i] + k >= b_index[j] && a_index[i] - k <= b_index[j]) {
            result.push(a_index[i]);
            i++;
        } else if (a_index[i] - k > b_index[j]) {
            j++;
        } else {
            i++;
        }
    }
    return result;
};
