// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

/**
 * @param {number} n
 * @param {number[][]} meetings
 * @param {number} firstPerson
 * @return {number[]}
 */
var findAllPeople = function(n, meetings, firstPerson) {
    meetings.sort((a, b) => a[2] - b[2]);
    const parent = Array.from({length: n}, (_, i) => i);
    const find = (x) => parent[x] === x ? x : (parent[x] = find(parent[x]));
    const unite = (a, b) => {
        a = find(a); b = find(b);
        if (a !== b) parent[a] = b;
    };
    const know = new Array(n).fill(false);
    know[0] = know[firstPerson] = true;
    unite(0, firstPerson);
    for (let i = 0; i < meetings.length; ) {
        let j = i;
        while (j < meetings.length && meetings[j][2] === meetings[i][2]) j++;
        for (let k = i; k < j; k++) unite(meetings[k][0], meetings[k][1]);
        const root0 = find(0);
        const reset = [];
        for (let k = i; k < j; k++) {
            const a = meetings[k][0], b = meetings[k][1];
            if (find(a) !== root0) { reset.push(a); reset.push(b); }
            else { know[a] = know[b] = true; }
        }
        for (const x of reset) parent[x] = x;
        i = j;
    }
    const ans = [];
    for (let i = 0; i < n; i++) if (find(i) === find(0) || know[i]) ans.push(i);
    return ans;
};
