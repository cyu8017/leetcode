// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

function maxDepth(s: string): number {
    let depth = 0, ans = 0;
    for (const ch of s) {
        if (ch === "(") {
            depth++;
            ans = Math.max(ans, depth);
        } else if (ch === ")") depth--;
    }
    return ans;
}
