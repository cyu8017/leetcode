export class Twitter {
    private time = 0;
    private tweets = new Map<number, Array<[number, number]>>();
    private following = new Map<number, Set<number>>();

    postTweet(userId: number, tweetId: number): void {
        this.time += 1;
        if (!this.tweets.has(userId)) this.tweets.set(userId, []);
        this.tweets.get(userId)!.push([this.time, tweetId]);
    }

    getNewsFeed(userId: number): number[] {
        const heap: Array<[number, number]> = [];
        const users = new Set([...(this.following.get(userId) ?? []), userId]);

        for (const uid of users) {
            for (const [timestamp, tweetId] of (this.tweets.get(uid) ?? []).slice(-10)) {
                heap.push([-timestamp, tweetId]);
            }
        }

        heap.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
        const feed: number[] = [];
        while (heap.length && feed.length < 10) feed.push(heap.shift()![1]);
        return feed;
    }

    follow(followerId: number, followeeId: number): void {
        if (!this.following.has(followerId)) this.following.set(followerId, new Set());
        this.following.get(followerId)!.add(followeeId);
    }

    unfollow(followerId: number, followeeId: number): void {
        this.following.get(followerId)?.delete(followeeId);
    }
}
