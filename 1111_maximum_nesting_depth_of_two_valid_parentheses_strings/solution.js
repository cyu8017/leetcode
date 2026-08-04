// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

/**
 * @param {string} seq
 * @return {number[]}
 */
var maxDepthAfterSplit = function(seq) {
    let depth = 0;
    const ans = Array(seq.length).fill(0);
    for (let i = 0; i < seq.length; i++) {
        if (seq[i] === "(") {
            ans[i] = depth % 2;
            depth++;
        } else {
            depth--;
            ans[i] = depth % 2;
        }
    }
    return ans;
};
