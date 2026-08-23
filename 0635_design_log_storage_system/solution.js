// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

var LogSystem = function() {
    this.ids = [];
    this.timestamps = [];
    this.granularityIndex = {
        Year: 4, Month: 7, Day: 10, Hour: 13, Minute: 16, Second: 19
    };
};

/**
 * @param {number} id
 * @param {string} timestamp
 * @return {void}
 */
LogSystem.prototype.put = function(id, timestamp) {
    this.ids.push(id);
    this.timestamps.push(timestamp);
};

/**
 * @param {string} start
 * @param {string} end
 * @param {string} granularity
 * @return {number[]}
 */
LogSystem.prototype.retrieve = function(start, end, granularity) {
    const index = this.granularityIndex[granularity];
    const startKey = start.substring(0, index);
    const endKey = end.substring(0, index);
    const matched = [];
    for (let i = 0; i < this.timestamps.length; ++i) {
        const timestamp = this.timestamps[i];
        const key = timestamp.substring(0, index);
        if (startKey <= key && key <= endKey) matched.push([timestamp, this.ids[i]]);
    }
    matched.sort((a, b) => a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0);
    return matched.map((item) => item[1]);
};
