# LeetCode 3527 - Find the Most Common Response
# https://leetcode.com/problems/find-the-most-common-response/

# @param {String[][]} responses
# @return {String}
def find_common_response(responses)
  cnt = {}
  responses.each do |ws|
    seen = {}
    ws.each do |w|
      next if seen[w]
      seen[w] = true
      cnt[w] = (cnt[w] || 0) + 1
    end
  end
  ans = responses[0][0]
  cnt.each do |w, v|
    ans = w if cnt[ans] < v || (cnt[ans] == v && w < ans)
  end
  ans
end
