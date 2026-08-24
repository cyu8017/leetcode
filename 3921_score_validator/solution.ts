// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

export function scoreValidator(events: any): any {
    let score = 0, counter = 0;
    for (const eventStr of events) {
        let isNum = eventStr.length > 0;
        let num = 0;
        let start = 0;
        if (isNum && eventStr[0] === '-') start = 1;
        for (let i = start; i < eventStr.length; i++) {
            if (eventStr[i] < '0' || eventStr[i] > '9') {
                isNum = false;
                break;
            }
            num = num * 10 + (eventStr.charCodeAt(i) - 48);
        }
        if (isNum && !(start === 1 && eventStr.length === 1)) {
            if (start === 1) num = -num;
            score += num;
        } else if (eventStr === 'W') {
            counter++;
            if (counter === 10) break;
        } else {
            score++;
        }
    }
    return [score, counter];
}
