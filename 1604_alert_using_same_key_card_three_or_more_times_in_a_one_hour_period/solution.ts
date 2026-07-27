// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

function alertNames(keyName: string[], keyTime: string[]): string[] {
    const times = new Map<string, number[]>();
    for (let i = 0; i < keyName.length; i++) {
        const [h, m] = keyTime[i].split(":").map(Number);
        if (!times.has(keyName[i])) times.set(keyName[i], []);
        times.get(keyName[i])!.push(h * 60 + m);
    }
    const ans: string[] = [];
    for (const [name, a] of times) {
        a.sort((x, y) => x - y);
        let alert = false;
        for (let i = 0; i + 2 < a.length; i++) {
            if (a[i + 2] - a[i] <= 60) {
                alert = true;
                break;
            }
        }
        if (alert) ans.push(name);
    }
    return ans.sort();
}
