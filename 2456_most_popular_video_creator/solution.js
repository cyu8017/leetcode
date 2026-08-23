// LeetCode 2456 - Most Popular Video Creator
// https://leetcode.com/problems/most-popular-video-creator/

/**
 * @param {string[]} creators
 * @param {string[]} ids
 * @param {number[]} views
 * @return {string[][]}
 */
var mostPopularCreator = function(creators, ids, views) {
    const mp = new Map();
    let maxTotal = 0;
    for (let i = 0; i < creators.length; i++) {
        let info = mp.get(creators[i]);
        if (!info) {
            info = { total: views[i], bestID: ids[i], bestViews: views[i] };
            mp.set(creators[i], info);
        } else {
            info.total += views[i];
            if (views[i] > info.bestViews ||
                (views[i] === info.bestViews && ids[i] < info.bestID)) {
                info.bestViews = views[i];
                info.bestID = ids[i];
            }
        }
        maxTotal = Math.max(maxTotal, mp.get(creators[i]).total);
    }
    const ans = [];
    for (const [creator, info] of mp) {
        if (info.total === maxTotal) ans.push([creator, info.bestID]);
    }
    return ans;
};
