// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

var countMentions = function(numberOfUsers, events) {
    events = events.slice().sort((a, b) => {
        const ti = parseInt(a[1], 10), tj = parseInt(b[1], 10);
        if (ti !== tj) return ti - tj;
        return b[0].localeCompare(a[0]);
    });
    const online = new Array(numberOfUsers).fill(true);
    const offlineUntil = new Array(numberOfUsers).fill(0);
    const ans = new Array(numberOfUsers).fill(0);
    for (const e of events) {
        const t = parseInt(e[1], 10);
        for (let i = 0; i < numberOfUsers; i++) {
            if (!online[i] && offlineUntil[i] <= t) online[i] = true;
        }
        if (e[0] === "OFFLINE") {
            const id = parseInt(e[2], 10);
            online[id] = false;
            offlineUntil[id] = t + 60;
        } else {
            const msg = e[2];
            if (msg === "ALL") {
                for (let i = 0; i < numberOfUsers; i++) ans[i]++;
            } else if (msg === "HERE") {
                for (let i = 0; i < numberOfUsers; i++) if (online[i]) ans[i]++;
            } else {
                for (const part of msg.split(" ")) {
                    const id = parseInt(part.substring(2), 10);
                    ans[id]++;
                }
            }
        }
    }
    return ans;
};
