// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

export function processStr(s: any): any {
    let result = [];
    for (const c of s) {
        if (/[a-zA-Z]/.test(c)) result.push(c);
        else if (c === '*') {
            if (result.length > 0) result.pop();
        } else if (c === '#') result = result.concat(result);
        else if (c === '%') result.reverse();
    }
    return result.join('');
}
