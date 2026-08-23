// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

/**
 * @param {string[][]} accounts
 * @return {string[][]}
 */
var accountsMerge = function(accounts) {
    const parent = new Map();
    const find = (x) => {
        if (!parent.has(x)) parent.set(x, x);
        while (parent.get(x) !== x) {
            parent.set(x, parent.get(parent.get(x)));
            x = parent.get(x);
        }
        return x;
    };
    const unite = (a, b) => { parent.set(find(a), find(b)); };
    const emailName = new Map();
    for (const account of accounts) {
        const name = account[0], first = account[1];
        for (let i = 1; i < account.length; i++) {
            const email = account[i];
            if (!parent.has(email)) parent.set(email, email);
            emailName.set(email, name);
            unite(first, email);
        }
    }
    const groups = new Map();
    for (const email of parent.keys()) {
        const root = find(email);
        if (!groups.has(root)) groups.set(root, []);
        groups.get(root).push(email);
    }
    const result = [];
    for (const emails of groups.values()) {
        emails.sort();
        result.push([emailName.get(emails[0]), ...emails]);
    }
    return result;
};
