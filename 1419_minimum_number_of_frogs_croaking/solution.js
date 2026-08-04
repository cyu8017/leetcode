// LeetCode 1419: Minimum Number Of Frogs Croaking

var minNumberOfFrogs = function(croakOfFrogs) {
    const order = "croak", count = Array(5).fill(0);
    let active = 0, maximum = 0;
    for (const ch of croakOfFrogs) {
        const index = order.indexOf(ch);
        if (index === 0) { count[0]++; active++; maximum = Math.max(maximum, active); }
        else { if (count[index - 1] === 0) return -1; count[index - 1]--; if (index === 4) active--; else count[index]++; }
    }
    return active === 0 ? maximum : -1;
};
