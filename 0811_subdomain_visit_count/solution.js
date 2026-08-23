// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

/**
 * @param {string[]} cpdomains
 * @return {string[]}
 */
var subdomainVisits = function(cpdomains) {
    const counts = new Map();
    for (const item of cpdomains) {
        const space = item.indexOf(' ');
        const count = parseInt(item.substring(0, space), 10);
        let domain = item.substring(space + 1);
        while (true) {
            counts.set(domain, (counts.get(domain) || 0) + count);
            const dot = domain.indexOf('.');
            if (dot < 0) break;
            domain = domain.substring(dot + 1);
        }
    }
    const ans = [];
    for (const [key, value] of counts) ans.push(value + " " + key);
    return ans;
};
