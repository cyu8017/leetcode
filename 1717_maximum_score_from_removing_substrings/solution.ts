// LeetCode 1717 - Maximum Score From Removing Substrings
// https://leetcode.com/problems/maximum-score-from-removing-substrings/

function maximumGain(s: string, x: number, y: number): number {
    const remove = (text: string, pair: string, score: number): [string, number] => {
        const stack: string[] = [];
        let gained = 0;
        for (const ch of text) {
            if (stack.length > 0 && stack[stack.length - 1] === pair[0] && ch === pair[1]) {
                stack.pop();
                gained += score;
            } else {
                stack.push(ch);
            }
        }
        return [stack.join(''), gained];
    };

    let rest: string;
    let first: number;
    let second: number;
    if (x >= y) {
        [rest, first] = remove(s, 'ab', x);
        [, second] = remove(rest, 'ba', y);
    } else {
        [rest, first] = remove(s, 'ba', y);
        [, second] = remove(rest, 'ab', x);
    }
    return first + second;
}
