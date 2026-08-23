// LeetCode 2284 - Sender With Largest Word Count
// https://leetcode.com/problems/sender-with-largest-word-count/

var largestWordCount = function(messages, senders) {
    const count = new Map();
    let best = '', bestCnt = -1;
    for (let i = 0; i < messages.length; i++) {
        let words = 1;
        for (const c of messages[i]) if (c === ' ') words++;
        const c2 = (count.get(senders[i]) || 0) + words;
        count.set(senders[i], c2);
        if (c2 > bestCnt || (c2 === bestCnt && senders[i] > best)) {
            bestCnt = c2;
            best = senders[i];
        }
    }
    return best;
};
