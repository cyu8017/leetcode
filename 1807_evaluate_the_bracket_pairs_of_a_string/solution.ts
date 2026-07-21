// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

function evaluate(s: string, knowledge: string[][]): string {
    const lookup = new Map<string, string>();
    for (const [key, value] of knowledge) lookup.set(key, value);
    const result: string[] = [];
    let i = 0;
    while (i < s.length) {
        if (s[i] === '(') {
            const j = s.indexOf(')', i + 1);
            const key = s.slice(i + 1, j);
            result.push(lookup.has(key) ? lookup.get(key)! : '?');
            i = j + 1;
        } else {
            result.push(s[i]);
            i += 1;
        }
    }
    return result.join('');
}
