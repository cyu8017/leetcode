// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

export function applySubstitutions(replacements: any, text: any): any {
    const mp = new Map();
    for (const r of replacements) mp.set(r[0], r[1]);
    const resolve = (s) => {
        let out = "";
        for (let i = 0; i < s.length; ) {
            if (s[i] === "%") {
                let j = i + 1;
                while (j < s.length && s[j] !== "%") j++;
                const key = s.substring(i + 1, j);
                out += resolve(mp.get(key));
                i = j + 1;
            } else {
                out += s[i];
                i++;
            }
        }
        return out;
    };
    return resolve(text);
}
