# LeetCode 3295 - Report Spam Message
# https://leetcode.com/problems/report-spam-message/

# @param {String[]} message
# @param {String[]} banned_words
# @return {Boolean}
def report_spam(message, banned_words)
  ban = {}
  banned_words.each { |w| ban[w] = true }
  cnt = 0
  message.each do |w|
    if ban[w]
      cnt += 1
      return true if cnt >= 2
    end
  end
  false
end
