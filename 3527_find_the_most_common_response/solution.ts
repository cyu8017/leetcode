// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

export function findCommonResponse(responses: any): any {
    const cnt = new Map();
    for (const ws of responses) {
        const s = new Set();
        for (const w of ws) {
            if (!s.has(w)) {
                s.add(w);
                cnt.set(w, (cnt.get(w) || 0) + 1);
            }
        }
    }
    let ans = responses[0][0];
    for (const [w, v] of cnt) {
        if (cnt.get(ans) < v || (cnt.get(ans) === v && w < ans)) ans = w;
    }
    return ans;
}
