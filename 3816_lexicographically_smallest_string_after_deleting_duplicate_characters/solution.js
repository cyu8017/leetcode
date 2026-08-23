// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically_smallest_string_after_deleting_duplicate_characters/

var lexSmallestAfterDeletion = function(s) {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    const stk = [];
    for (const c of s) {
        while (stk.length > 0 && stk[stk.length - 1] > c
                && cnt[stk[stk.length - 1].charCodeAt(0) - 97] > 1) {
            cnt[stk[stk.length - 1].charCodeAt(0) - 97]--;
            stk.pop();
        }
        stk.push(c);
    }
    while (cnt[stk[stk.length - 1].charCodeAt(0) - 97] > 1) {
        cnt[stk[stk.length - 1].charCodeAt(0) - 97]--;
        stk.pop();
    }
    return stk.join('');
};
