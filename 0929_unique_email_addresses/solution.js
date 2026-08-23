// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

/**
 * @param {string[]} emails
 * @return {number}
 */
var numUniqueEmails = function(emails) {
    const set = new Set();
    for (const email of emails) {
        const [local, domain] = email.split("@");
        let cleaned = "";
        for (const ch of local) {
            if (ch === "+") break;
            if (ch !== ".") cleaned += ch;
        }
        set.add(cleaned + "@" + domain);
    }
    return set.size;
};
