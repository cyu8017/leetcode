// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

export function stringSequence(target: any): any {
    const ans = [];
    let cur = '';
    for (const ch of target) {
        cur += 'a';
        ans.push(cur);
        while (cur[cur.length - 1] !== ch) {
            const last = String.fromCharCode(cur.charCodeAt(cur.length - 1) + 1);
            cur = cur.slice(0, -1) + last;
            ans.push(cur);
        }
    }
    return ans;
}
