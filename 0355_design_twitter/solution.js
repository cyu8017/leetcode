// LeetCode 0355 - Design Twitter
class Twitter {
    constructor() {
        this.time = 0;
        this.tweets = new Map();
        this.following = new Map();
    }

    postTweet(userId, tweetId) {
        this.time += 1;
        if (!this.tweets.has(userId)) this.tweets.set(userId, []);
        this.tweets.get(userId).push([this.time, tweetId]);
    }

    getNewsFeed(userId) {
        const heap = [];
        const users = new Set([...(this.following.get(userId) || []), userId]);

        for (const uid of users) {
            for (const [timestamp, tweetId] of (this.tweets.get(uid) || []).slice(-10)) {
                heap.push([-timestamp, tweetId]);
            }
        }

        heap.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
        const feed = [];
        while (heap.length && feed.length < 10) {
            feed.push(heap.shift()[1]);
        }
        return feed;
    }

    follow(followerId, followeeId) {
        if (!this.following.has(followerId)) this.following.set(followerId, new Set());
        this.following.get(followerId).add(followeeId);
    }

    unfollow(followerId, followeeId) {
        this.following.get(followerId)?.delete(followeeId);
    }
}

module.exports = { Twitter };
