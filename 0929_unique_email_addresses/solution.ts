// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

export function numUniqueEmails(emails: string[]): number {
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
}
