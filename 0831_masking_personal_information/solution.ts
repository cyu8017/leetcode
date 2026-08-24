// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

export function maskPII(s: string): string {
    let at = s.indexOf('@');
    if (at >= 0) {
        s = s.toLowerCase();
        at = s.indexOf('@');
        const name = s.substring(0, at);
        const domain = s.substring(at + 1);
        return name[0] + "*****" + name[name.length - 1] + "@" + domain;
    }
    let digits = "";
    for (const ch of s) if (/\d/.test(ch)) digits += ch;
    const local = digits.substring(digits.length - 4);
    const country = digits.length - 10;
    if (country === 0) return "***-***-" + local;
    return "+" + "*".repeat(country) + "-***-***-" + local;
}
