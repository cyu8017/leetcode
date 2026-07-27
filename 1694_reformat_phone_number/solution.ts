// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

function reformatNumber(number: string): string {
    let s = [...number].filter((c) => c >= "0" && c <= "9").join("");
    const out: string[] = [];
    while (s.length > 4) {
        out.push(s.slice(0, 3));
        s = s.slice(3);
    }
    if (s.length === 4) out.push(s.slice(0, 2), s.slice(2));
    else if (s) out.push(s);
    return out.join("-");
}
