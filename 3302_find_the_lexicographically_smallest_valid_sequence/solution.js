// LeetCode 3302 - Find the Lexicographically Smallest Valid Sequence
// https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/

function canFinish(w1, w2, i, j, usedSkip, right) {
    const m = w2.length;
    if (j >= m) return true;
    if (!usedSkip) {
        if (right[j] >= i) return true;
        if (j + 1 <= m && right[j + 1] > i) return true;
        if (right[j] > i) return true;
        return false;
    }
    return right[j] >= i;
}
var validSequence = function(word1, word2) {
    const n = word1.length, m = word2.length;
    const right = new Array(m + 1);
    right[m] = n;
    let j = m - 1;
    for (let i = n - 1; i >= 0 && j >= 0; i--) {
        if (word1[i] === word2[j]) {
            right[j] = i;
            j--;
        }
    }
    for (; j >= 0; j--) right[j] = -1;
    const ans = new Array(m);
    let usedSkip = false;
    let i = 0;
    for (j = 0; j < m; j++) {
        let found = false;
        while (i < n) {
            if (word1[i] === word2[j]) {
                if (canFinish(word1, word2, i + 1, j + 1, usedSkip, right)) {
                    ans[j] = i;
                    i++;
                    found = true;
                    break;
                }
            } else if (!usedSkip) {
                if (canFinish(word1, word2, i + 1, j + 1, true, right)) {
                    ans[j] = i;
                    i++;
                    usedSkip = true;
                    found = true;
                    break;
                }
            }
            i++;
        }
        if (!found) return [];
    }
    return ans;
};
