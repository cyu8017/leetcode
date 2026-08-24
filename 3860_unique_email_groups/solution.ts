// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

export function uniqueEmailGroups(emails: any): any {
    const st = new Set();
    for (const email of emails) {
        const at = email.indexOf('@');
        let local = email.substring(0, at);
        const domain = email.substring(at + 1).toLowerCase();
        const plus = local.indexOf('+');
        if (plus >= 0) local = local.substring(0, plus);
        let cleaned = '';
        for (const c of local) if (c !== '.') cleaned += c.toLowerCase();
        st.add(cleaned + domain);
    }
    return st.size;
}
