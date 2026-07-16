# LeetCode 0355 - Design Twitter
# https://leetcode.com/problems/design-twitter/

class Twitter
  def initialize
    @time = 0
    @tweets = Hash.new { |hash, key| hash[key] = [] }
    @following = Hash.new { |hash, key| hash[key] = {} }
  end

  def post_tweet(user_id, tweet_id)
    @time += 1
    @tweets[user_id] << [@time, tweet_id]
  end

  def get_news_feed(user_id)
    users = @following[user_id].keys + [user_id]
    candidates = []

    users.each do |uid|
      @tweets[uid].last(10).each do |timestamp, tweet_id|
        candidates << [timestamp, tweet_id]
      end
    end

    candidates.sort_by { |timestamp, _| -timestamp }.first(10).map(&:last)
  end

  def follow(follower_id, followee_id)
    @following[follower_id][followee_id] = true
  end

  def unfollow(follower_id, followee_id)
    @following[follower_id].delete(followee_id)
  end

  alias_method :postTweet, :post_tweet
  alias_method :getNewsFeed, :get_news_feed
end
