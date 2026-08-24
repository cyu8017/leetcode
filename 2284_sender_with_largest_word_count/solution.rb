# LeetCode 2284 - Sender With Largest Word Count
# https://leetcode.com/problems/sender-with-largest-word-count/

# @param {String[]} messages
# @param {String[]} senders
# @return {String}
def largest_word_count(messages, senders)
  count = Hash.new(0)
  best = ""
  best_cnt = -1
  messages.each_with_index do |msg, i|
    words = 1
    msg.each_char { |c| words += 1 if c == " " }
    c2 = count[senders[i]] + words
    count[senders[i]] = c2
    if c2 > best_cnt || (c2 == best_cnt && senders[i] > best)
      best_cnt = c2
      best = senders[i]
    end
  end
  best
end
