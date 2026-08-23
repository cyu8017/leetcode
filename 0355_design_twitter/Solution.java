// LeetCode 0355 - Design Twitter

// https://leetcode.com/problems/design-twitter/



import java.util.ArrayList;

import java.util.HashMap;

import java.util.HashSet;

import java.util.List;

import java.util.Map;

import java.util.PriorityQueue;

import java.util.Set;



class Twitter {

    private int time;

    private final Map<Integer, List<int[]>> tweets = new HashMap<>();

    private final Map<Integer, Set<Integer>> following = new HashMap<>();



    public Twitter() {

        this.time = 0;

    }



    public void postTweet(int userId, int tweetId) {

        time++;

        tweets.computeIfAbsent(userId, key -> new ArrayList<>())

            .add(new int[] {time, tweetId});

    }



    public List<Integer> getNewsFeed(int userId) {

        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));

        Set<Integer> users = new HashSet<>(following.getOrDefault(userId, Set.of()));

        users.add(userId);



        for (int uid : users) {

            List<int[]> userTweets = tweets.get(uid);

            if (userTweets == null) {

                continue;

            }



            int start = Math.max(0, userTweets.size() - 10);

            for (int index = start; index < userTweets.size(); index++) {

                heap.offer(userTweets.get(index));

            }

        }



        List<Integer> feed = new ArrayList<>();

        while (!heap.isEmpty() && feed.size() < 10) {

            feed.add(heap.poll()[1]);

        }



        return feed;

    }



    public void follow(int followerId, int followeeId) {

        following.computeIfAbsent(followerId, key -> new HashSet<>()).add(followeeId);

    }



    public void unfollow(int followerId, int followeeId) {

        Set<Integer> followees = following.get(followerId);

        if (followees != null) {

            followees.remove(followeeId);

        }

    }

}
