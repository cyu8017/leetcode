// LeetCode 0355 - Design Twitter

// https://leetcode.com/problems/design-twitter/



using System.Collections.Generic;



public class Twitter {

    private int time;

    private readonly Dictionary<int, List<int[]>> tweets = new();

    private readonly Dictionary<int, HashSet<int>> following = new();



    public Twitter() {

        this.time = 0;

    }



    public void PostTweet(int userId, int tweetId) {

        time++;

        if (!tweets.ContainsKey(userId)) {

            tweets[userId] = new List<int[]>();

        }

        tweets[userId].Add(new int[] {time, tweetId});

    }



    public IList<int> GetNewsFeed(int userId) {

        PriorityQueue<int[], int> heap = new();

        HashSet<int> users = following.ContainsKey(userId)

            ? new HashSet<int>(following[userId])

            : new HashSet<int>();

        users.Add(userId);



        foreach (int uid in users) {

            if (!tweets.ContainsKey(uid)) {

                continue;

            }



            List<int[]> userTweets = tweets[uid];

            int start = Math.Max(0, userTweets.Count - 10);

            for (int index = start; index < userTweets.Count; index++) {

                heap.Enqueue(userTweets[index], -userTweets[index][0]);

            }

        }



        List<int> feed = new();

        while (heap.Count > 0 && feed.Count < 10) {

            feed.Add(heap.Dequeue()[1]);

        }



        return feed;

    }



    public void Follow(int followerId, int followeeId) {

        if (!following.ContainsKey(followerId)) {

            following[followerId] = new HashSet<int>();

        }

        following[followerId].Add(followeeId);

    }



    public void Unfollow(int followerId, int followeeId) {

        if (following.ContainsKey(followerId)) {

            following[followerId].Remove(followeeId);

        }

    }

}
